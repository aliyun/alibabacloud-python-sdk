# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_appstream_center20210218 import models as main_models
from darabonba.model import DaraModel

class GetLatestThirdAppAccessTokenRequest(DaraModel):
    def __init__(
        self,
        authorizer_id: str = None,
        business_channel: str = None,
        resource: main_models.GetLatestThirdAppAccessTokenRequestResource = None,
    ):
        # The WyId of the user used when the token was created. It must correspond to the current account and the target cloud desktop, and cannot be replaced by a username.
        # 
        # This parameter is required.
        self.authorizer_id = authorizer_id
        # The business channel. Valid values: Enterprise and Business. The value is case-insensitive. If omitted, the default value is Enterprise. If an empty string or other value is explicitly passed, a parameter error is returned. This parameter does not replace user identity verification.
        self.business_channel = business_channel
        # The target single cloud desktop resource. You must provide this object along with ResourceType and ResourceId when calling this operation. Pass it as a JSON object to specify only one cloud desktop. Wildcards or authorization for all cloud desktops are not supported.
        self.resource = resource

    def validate(self):
        if self.resource:
            self.resource.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorizer_id is not None:
            result['AuthorizerId'] = self.authorizer_id

        if self.business_channel is not None:
            result['BusinessChannel'] = self.business_channel

        if self.resource is not None:
            result['Resource'] = self.resource.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizerId') is not None:
            self.authorizer_id = m.get('AuthorizerId')

        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('Resource') is not None:
            temp_model = main_models.GetLatestThirdAppAccessTokenRequestResource()
            self.resource = temp_model.from_map(m.get('Resource'))

        return self

class GetLatestThirdAppAccessTokenRequestResource(DaraModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The ID of the cloud desktop specified when the token was created. You must provide a non-empty value that is consistent with the value used during creation. Asterisks (*) are not allowed.
        self.resource_id = resource_id
        # The resource type. This parameter is required. Valid value: DESKTOP, which indicates a cloud desktop. The value is case-insensitive.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

