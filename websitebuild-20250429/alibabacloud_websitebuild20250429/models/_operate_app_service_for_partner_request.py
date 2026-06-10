# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OperateAppServiceForPartnerRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        extend: str = None,
        operate_event: str = None,
        service_type: str = None,
    ):
        # Business ID.
        self.biz_id = biz_id
        # Additional extension information in JSON structure, facilitating future parameter extensions.
        self.extend = extend
        # Operation event:  
        # SERVICE_FINISH: Service completed
        self.operate_event = operate_event
        # Service Type.  
        # 
        # Valid values:  
        # 
        # - private: Deployed under the user\\"s account.  
        # 
        # - managed: Hosted under the service provider\\"s account.  
        # 
        # - operation: Alibaba Cloud Managed Services.
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.operate_event is not None:
            result['OperateEvent'] = self.operate_event

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('OperateEvent') is not None:
            self.operate_event = m.get('OperateEvent')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        return self

