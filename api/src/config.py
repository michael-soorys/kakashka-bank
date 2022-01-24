import os


class Config():

  @staticmethod
  def __getDevConfig():
    return {
      'env': 'dev',
      'dbCollection': 'userDataDev'
    }
    

  @staticmethod
  def __getProdConfig():
    return {
      'env': 'prod',
      'dbCollection': 'userData'
    }

  @staticmethod
  def getConfig(env:str):
    if not env and str != 'DEV' and str != 'PROD':
      raise Exception(f"No environment specified. You need to export FLASK_ENV to be either DEV or PROD, instead we got {env}")
    if env == 'DEV': return Config.__getDevConfig()
    if env == 'PROD': return Config.__getProdConfig()
