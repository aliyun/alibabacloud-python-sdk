# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListVersionDistributionRequest(DaraModel):
    def __init__(
        self,
        client_type: int = None,
        in_manage: bool = None,
        main_biz_type: str = None,
        model: str = None,
        version_type: str = None,
    ):
        # The terminal type. Valid values:
        # - 1: hardware terminal.
        # - 2: software terminal.
        # - 3: secure browser plugin.
        # - 4: GuestOS application.
        # - 5: DingTalk Wuying plugin.
        # - 6: cloud application component.
        # - 7: Cloud Hub.
        # - 8: H5.
        # 
        # This parameter is required.
        self.client_type = client_type
        # The management status. A value of true indicates managed, and a value of false indicates unmanaged. If this parameter is not specified, all terminals are queried.
        self.in_manage = in_manage
        # The business type. Default value: enterprise.
        self.main_biz_type = main_biz_type
        # The terminal model.
        # 
        # This parameter is required.
        self.model = model
        # The version type. Valid values:
        # - SYS: system version.
        # - APP: application version.
        # 
        # This parameter is required.
        self.version_type = version_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_type is not None:
            result['ClientType'] = self.client_type

        if self.in_manage is not None:
            result['InManage'] = self.in_manage

        if self.main_biz_type is not None:
            result['MainBizType'] = self.main_biz_type

        if self.model is not None:
            result['Model'] = self.model

        if self.version_type is not None:
            result['VersionType'] = self.version_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')

        if m.get('InManage') is not None:
            self.in_manage = m.get('InManage')

        if m.get('MainBizType') is not None:
            self.main_biz_type = m.get('MainBizType')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')

        return self

