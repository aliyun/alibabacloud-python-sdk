# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ListTenantConfigResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        tenant_config_model: main_models.ListTenantConfigResponseBodyTenantConfigModel = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The user configuration information.
        self.tenant_config_model = tenant_config_model

    def validate(self):
        if self.tenant_config_model:
            self.tenant_config_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tenant_config_model is not None:
            result['TenantConfigModel'] = self.tenant_config_model.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TenantConfigModel') is not None:
            temp_model = main_models.ListTenantConfigResponseBodyTenantConfigModel()
            self.tenant_config_model = temp_model.from_map(m.get('TenantConfigModel'))

        return self

class ListTenantConfigResponseBodyTenantConfigModel(DaraModel):
    def __init__(
        self,
        app_instance_group_expire_remind: bool = None,
        multi_session_support_type: str = None,
        multi_session_supported_regions: List[str] = None,
    ):
        # Indicates whether resource expiration reminders are enabled. Valid values:
        # 
        # - true: Enabled.
        # - false: Not enabled.
        self.app_instance_group_expire_remind = app_instance_group_expire_remind
        self.multi_session_support_type = multi_session_support_type
        self.multi_session_supported_regions = multi_session_supported_regions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_group_expire_remind is not None:
            result['AppInstanceGroupExpireRemind'] = self.app_instance_group_expire_remind

        if self.multi_session_support_type is not None:
            result['MultiSessionSupportType'] = self.multi_session_support_type

        if self.multi_session_supported_regions is not None:
            result['MultiSessionSupportedRegions'] = self.multi_session_supported_regions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceGroupExpireRemind') is not None:
            self.app_instance_group_expire_remind = m.get('AppInstanceGroupExpireRemind')

        if m.get('MultiSessionSupportType') is not None:
            self.multi_session_support_type = m.get('MultiSessionSupportType')

        if m.get('MultiSessionSupportedRegions') is not None:
            self.multi_session_supported_regions = m.get('MultiSessionSupportedRegions')

        return self

