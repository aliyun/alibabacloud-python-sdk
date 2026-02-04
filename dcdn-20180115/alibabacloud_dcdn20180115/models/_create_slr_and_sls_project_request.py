# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSlrAndSlsProjectRequest(DaraModel):
    def __init__(
        self,
        business_type: str = None,
        region: str = None,
    ):
        # The type of the collected logs. Default value: cdn_log_access_l1. Valid values:
        # 
        # *   **cdn_log_access_l1**: access logs of L1 Dynamic Route for CDN (DCDN) points of presence (POPs)
        # *   **cdn_log_origin**: back-to-origin logs
        # *   **cdn_log_er**: EdgeRoutine logs
        self.business_type = business_type
        # The region where Log Service resides. Valid values:
        # 
        # *   **cn-hangzhou**
        # *   **cn-shanghai**
        # *   **cn-qingdao**
        # *   **cn-beijing**
        # *   **cn-zhangjiakou**
        # *   **cn-shenzhen**
        # *   **eu-central-1**
        # *   **us-west-1**
        # *   **ap-south-1**
        # *   **ap-southeast-1**
        # 
        # This parameter is required.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

