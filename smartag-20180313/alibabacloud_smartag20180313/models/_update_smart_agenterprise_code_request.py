# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSmartAGEnterpriseCodeRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        enterprise_code: str = None,
        region_id: str = None,
        smart_agid: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The enterprise code with you want to associate the SAG APP instance.
        # 
        # This parameter is required.
        self.enterprise_code = enterprise_code
        # The ID of the region where the SAG APP instance is deployed.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the SAG APP instance.
        # 
        # This parameter is required.
        self.smart_agid = smart_agid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.enterprise_code is not None:
            result['EnterpriseCode'] = self.enterprise_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.smart_agid is not None:
            result['SmartAGId'] = self.smart_agid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EnterpriseCode') is not None:
            self.enterprise_code = m.get('EnterpriseCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SmartAGId') is not None:
            self.smart_agid = m.get('SmartAGId')

        return self

