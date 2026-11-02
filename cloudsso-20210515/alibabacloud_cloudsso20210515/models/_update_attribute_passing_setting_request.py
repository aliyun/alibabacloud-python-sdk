# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAttributePassingSettingRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        source_identity_passing: str = None,
    ):
        # The directory ID.
        self.directory_id = directory_id
        # The SourceIdentity pass-through mode. Three pass-through modes are supported. If this parameter is not specified, the existing configuration is not modified.
        # 
        # Valid values:
        # 
        # - IdP: Uses the SourceIdentity attribute value carried in the SAML assertion from the external identity provider (IdP). The attribute value must be 2 to 64 characters in length and can contain only letters, digits, and the following special characters: =,.@-_.
        # - UserName: Uses the CloudSSO username as the SourceIdentity. The system automatically adds a reserved prefix, resulting in the format acs:sso:<username>, with a total length of no more than 64 characters.
        # - Disabled: Does not pass through SourceIdentity.
        self.source_identity_passing = source_identity_passing

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.source_identity_passing is not None:
            result['SourceIdentityPassing'] = self.source_identity_passing

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('SourceIdentityPassing') is not None:
            self.source_identity_passing = m.get('SourceIdentityPassing')

        return self

