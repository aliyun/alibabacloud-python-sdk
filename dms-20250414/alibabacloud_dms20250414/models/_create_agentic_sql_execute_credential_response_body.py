# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class CreateAgenticSqlExecuteCredentialResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.CreateAgenticSqlExecuteCredentialResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The temporary credential information.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message returned if the call fails.
        self.error_message = error_message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # - **true**: The request is successful.                                 
        # - **false**: The request fails.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.CreateAgenticSqlExecuteCredentialResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateAgenticSqlExecuteCredentialResponseBodyData(DaraModel):
    def __init__(
        self,
        access_key: str = None,
        access_secret: str = None,
        catalog_name: str = None,
        catalog_uuid: str = None,
        database_uuid: str = None,
        expire_time: str = None,
        max_connect_times: int = None,
        qualified_name: str = None,
    ):
        # The AccessKey of the credential.
        self.access_key = access_key
        # The AccessKey secret of the credential. This value is returned only once when the credential is created. Keep it secure.
        self.access_secret = access_secret
        # The name of the instance.
        self.catalog_name = catalog_name
        # The UUID of the instance.
        self.catalog_uuid = catalog_uuid
        # The UUID of the database. If the credential is at the instance level, this value is empty.
        self.database_uuid = database_uuid
        # The expiration time of the credential. Format: yyyy-MM-dd HH:mm:ss.
        self.expire_time = expire_time
        # The total number of connections supported by the credential.
        self.max_connect_times = max_connect_times
        # The fully qualified name of the database. If the credential is at the instance level, this value is empty.
        self.qualified_name = qualified_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key is not None:
            result['AccessKey'] = self.access_key

        if self.access_secret is not None:
            result['AccessSecret'] = self.access_secret

        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name

        if self.catalog_uuid is not None:
            result['CatalogUuid'] = self.catalog_uuid

        if self.database_uuid is not None:
            result['DatabaseUuid'] = self.database_uuid

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.max_connect_times is not None:
            result['MaxConnectTimes'] = self.max_connect_times

        if self.qualified_name is not None:
            result['QualifiedName'] = self.qualified_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')

        if m.get('AccessSecret') is not None:
            self.access_secret = m.get('AccessSecret')

        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')

        if m.get('CatalogUuid') is not None:
            self.catalog_uuid = m.get('CatalogUuid')

        if m.get('DatabaseUuid') is not None:
            self.database_uuid = m.get('DatabaseUuid')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('MaxConnectTimes') is not None:
            self.max_connect_times = m.get('MaxConnectTimes')

        if m.get('QualifiedName') is not None:
            self.qualified_name = m.get('QualifiedName')

        return self

