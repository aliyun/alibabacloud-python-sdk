# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class GetAttributePassingSettingResponseBody(DaraModel):
    def __init__(
        self,
        attribute_passing_setting: main_models.GetAttributePassingSettingResponseBodyAttributePassingSetting = None,
        request_id: str = None,
    ):
        # The attribute passing settings.
        self.attribute_passing_setting = attribute_passing_setting
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.attribute_passing_setting:
            self.attribute_passing_setting.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute_passing_setting is not None:
            result['AttributePassingSetting'] = self.attribute_passing_setting.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributePassingSetting') is not None:
            temp_model = main_models.GetAttributePassingSettingResponseBodyAttributePassingSetting()
            self.attribute_passing_setting = temp_model.from_map(m.get('AttributePassingSetting'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAttributePassingSettingResponseBodyAttributePassingSetting(DaraModel):
    def __init__(
        self,
        source_identity_passing: str = None,
    ):
        # The SourceIdentity pass-through mode. If not configured, Disabled is returned by default. Valid values:
        # 
        # - IdP: Uses the SourceIdentity attribute value carried in the SAML assertion from the external identity provider (IdP). The attribute value must be 2 to 64 characters in length and can contain only letters, digits, and the following special characters: =,.@-_.
        # - UserName: Uses the CloudSSO username as the SourceIdentity. The system automatically adds a reserved prefix, resulting in the format acs:sso:<username>. The total length cannot exceed 64 characters.
        # - Disabled: Does not pass through the SourceIdentity.
        self.source_identity_passing = source_identity_passing

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_identity_passing is not None:
            result['SourceIdentityPassing'] = self.source_identity_passing

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIdentityPassing') is not None:
            self.source_identity_passing = m.get('SourceIdentityPassing')

        return self

