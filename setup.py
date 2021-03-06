from distutils.core import setup
setup(
  name = 'blockchain_myananta',         
  packages = ['blockchain_myananta'],  
  version = '1.0',      
  license='mit',     
  description = 'myananata blockchain repository',   
  author = 'Pratham Manocha',                   
  author_email = 'pratham369@yahoo.com',     
  url = 'https://github.com/prathamystic/blockchain',   
  download_url = 'https://github.com/prathamystic/blockchain/archive/refs/tags/v_1.0.tar.gz',   
  keywords = ['Blockchain', 'API', 'Python'],  
  install_requires=['cryptography', 'pickle', 'SocketUtils'],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
