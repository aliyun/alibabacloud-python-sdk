# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadPCACertRequest(DaraModel):
    def __init__(
        self,
        cert: str = None,
        name: str = None,
        private_key: str = None,
        warehouse_id: int = None,
    ):
        # <UploadPCACertResponse>
        #     <RequestId>15C66C7B-671A-4297-9187-2C4477247A74</RequestId>
        # </UploadPCACertResponse>
        # 
        # This parameter is required.
        self.cert = cert
        # UploadPCACert
        self.name = name
        # Uploads a private certificate to a certificate repository.
        self.private_key = private_key
        # The ID of the repository.
        # 
        # >  You can call the [ListCertWarehouse](https://help.aliyun.com/document_detail/455805.html) operation to query the ID.
        # 
        # This parameter is required.
        self.warehouse_id = warehouse_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert is not None:
            result['Cert'] = self.cert

        if self.name is not None:
            result['Name'] = self.name

        if self.private_key is not None:
            result['PrivateKey'] = self.private_key

        if self.warehouse_id is not None:
            result['WarehouseId'] = self.warehouse_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cert') is not None:
            self.cert = m.get('Cert')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')

        if m.get('WarehouseId') is not None:
            self.warehouse_id = m.get('WarehouseId')

        return self

