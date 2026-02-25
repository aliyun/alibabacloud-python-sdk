# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_starrocks20221019 import models as main_models
from darabonba.model import DaraModel

class ListGatewayResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListGatewayResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListGatewayResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListGatewayResponseBodyData(DaraModel):
    def __init__(
        self,
        enable_public_net: bool = None,
        fe_node_number: int = None,
        gateway_id: str = None,
        gateway_name: str = None,
        gateway_type: str = None,
        internal_domain: str = None,
        internal_slb_id: str = None,
        privatezone_id: str = None,
        public_domain: str = None,
        public_slb_acl_id: str = None,
        public_slb_id: str = None,
    ):
        self.enable_public_net = enable_public_net
        self.fe_node_number = fe_node_number
        self.gateway_id = gateway_id
        self.gateway_name = gateway_name
        self.gateway_type = gateway_type
        self.internal_domain = internal_domain
        self.internal_slb_id = internal_slb_id
        # PrivatezoneId
        self.privatezone_id = privatezone_id
        self.public_domain = public_domain
        self.public_slb_acl_id = public_slb_acl_id
        self.public_slb_id = public_slb_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_public_net is not None:
            result['EnablePublicNet'] = self.enable_public_net

        if self.fe_node_number is not None:
            result['FeNodeNumber'] = self.fe_node_number

        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.gateway_name is not None:
            result['GatewayName'] = self.gateway_name

        if self.gateway_type is not None:
            result['GatewayType'] = self.gateway_type

        if self.internal_domain is not None:
            result['InternalDomain'] = self.internal_domain

        if self.internal_slb_id is not None:
            result['InternalSlbId'] = self.internal_slb_id

        if self.privatezone_id is not None:
            result['PrivatezoneId'] = self.privatezone_id

        if self.public_domain is not None:
            result['PublicDomain'] = self.public_domain

        if self.public_slb_acl_id is not None:
            result['PublicSlbAclId'] = self.public_slb_acl_id

        if self.public_slb_id is not None:
            result['PublicSlbId'] = self.public_slb_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnablePublicNet') is not None:
            self.enable_public_net = m.get('EnablePublicNet')

        if m.get('FeNodeNumber') is not None:
            self.fe_node_number = m.get('FeNodeNumber')

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('GatewayName') is not None:
            self.gateway_name = m.get('GatewayName')

        if m.get('GatewayType') is not None:
            self.gateway_type = m.get('GatewayType')

        if m.get('InternalDomain') is not None:
            self.internal_domain = m.get('InternalDomain')

        if m.get('InternalSlbId') is not None:
            self.internal_slb_id = m.get('InternalSlbId')

        if m.get('PrivatezoneId') is not None:
            self.privatezone_id = m.get('PrivatezoneId')

        if m.get('PublicDomain') is not None:
            self.public_domain = m.get('PublicDomain')

        if m.get('PublicSlbAclId') is not None:
            self.public_slb_acl_id = m.get('PublicSlbAclId')

        if m.get('PublicSlbId') is not None:
            self.public_slb_id = m.get('PublicSlbId')

        return self

