# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindAppDomainRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        domain_name: str = None,
        domain_type: str = None,
        extend: str = None,
        operate_type: str = None,
    ):
        # The business ID.
        self.biz_id = biz_id
        # The domain name.
        self.domain_name = domain_name
        # The domain management type. Valid values:
        # 
        # - CUSTOM
        # - PLATFORM_PREFIX
        # 
        # Default value: CUSTOM.
        self.domain_type = domain_type
        # The extended information (OverwriteExistingRecord).
        self.extend = extend
        # The operation type for domain binding.
        self.operate_type = operate_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.domain_type is not None:
            result['DomainType'] = self.domain_type

        if self.extend is not None:
            result['Extend'] = self.extend

        if self.operate_type is not None:
            result['OperateType'] = self.operate_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')

        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')

        return self

