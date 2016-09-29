Title: Code Block Test
Category: Testing

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

```python
import sys
import ldap3
import re
import ssl

from configparser import ConfigParser


class CAuthSession(object):
    def __init__(self, auth=None):
        # read the sysconfig file and get the server connection string
        self.config = ConfigParser()
        try:
            self.config.read_file(open('/etc/sysconfig/central-auth'))
        except Exception as e:
            print(e)
            sys.exit()
        self.servername = self.config.get('connection', 'servername')
        # create a connection to LDAP
        try:
            # set-up the connection
            tls = ldap3.Tls(validate=ssl.CERT_NONE,
                            version=ssl.PROTOCOL_TLSv1_2)
            self.server = ldap3.Server(self.servername, use_ssl=True, tls=tls)
            # to authenticate, or not to authenticate
            if auth:
                self.connection = ldap3.Connection(self.server,
                                                   authentication=ldap3.SASL,
                                                   sasl_mechanism='GSSAPI')
            else:
                self.connection = ldap3.Connection(self.server)
            # complete the connection
            self.connection.bind()
        except Exception as e:
            print(e)
            sys.exit()
```
