import instaloader
import credentials
import os

ig_username = credentials.ig_username
ig_password = credentials.ig_password

# https://www.travelandleisure.com/worlds-best/national-parks-in-america
# tags = ['yellowstonenationalpark', 'grandtetonnationalpark', 'katmainationalpark', 'rockymountainnationalpark'
#         'yosemitenationalpark', 'glaciernationalpark', 'denalinationalpark', 'greatsmokymountainsnationalpark',
#         'kenaifjordsnationalpark', 'zionnationalpark', 'grandcanyonnationalpark', 'olympicnationalpark',
#         'wrangellsteliasnationalpark', 'mountrainiernationalpark', 'glacierbaynationalpark', 'sequoianationalpark',
#         'acadianationalpark', 'shenandoahnationalpark', 'redwoodnationalpark', 'voyageursnationalpark',
#         'northcascadesnationalpark', 'brycecanyonnationalpark', 'archesnationalpark', 'kingscanyonnationalpark',
#         'mesaverdenationalpark']

usernames = ['usinterior', 'jasoninthewilderness']

def instaLogin(USER: str, PASSWORD: str):
    '''
    instaLogin
    params
        USER: str, instagram username
        PASSWORD: str, instagram password
    return
        ses: session object
    '''
    print("Logging in...")

    ses = instaloader.Instaloader(download_videos=False, download_video_thumbnails=False, download_comments=False, save_metadata=True)
    ses.context.sleep = False
    ses.login(USER, PASSWORD)

    print("...done")

    return ses

def getProfiles(ses: instaloader.instaloader.Instaloader, username, filename):
    '''
    getProfiles
    params
        ses: session object
        username: str, instagram username
        filename: str, filename to posts to
    return
        None
    '''
    profile = instaloader.Profile.from_username(ses.context, username)

    posts = profile.get_posts()

    prior_pwd = os.getcwd()
    current_pwd = os.path.join(prior_pwd, '{}/'.format(filename))
    os.chdir(current_pwd)

    for index, post in enumerate(posts, 1):
        print('Downloading Post #: {}'.format(index))
        ses.download_post(post, target='{}_{}'.format(profile.username, index))

    os.chdir(prior_pwd)


def main():
    session = instaLogin(ig_username, ig_password)

    if session.context.is_logged_in:
        getProfiles(session, usernames[2], 'images')
    else:
        raise Exception("Authentication failure!")


if __name__ == '__main__':
    main()

