# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SetTemplatePermissionRequest(DaraModel):
    def __init__(
        self,
        account_ids: List[str] = None,
        share_option: str = None,
        template_id: str = None,
        template_version: str = None,
        version_option: str = None,
    ):
        # The Alibaba Cloud accounts with or from which you want to share or unshare the template.\\
        # Valid values of N: 1, 2, 3, 4, and 5.
        # 
        # > - This parameter cannot be set to the ID of the Alibaba Cloud account that owns the template, or the RAM users of this Alibaba Cloud account.
        # > - When ShareOption is set to CancelSharing, you can unshare the template from all the specified Alibaba Cloud accounts by using an asterisk (\\*).
        # 
        # This parameter is required.
        self.account_ids = account_ids
        # The sharing option.
        # 
        # Valid values:
        # 
        # *   ShareToAccounts: shares the template with other Alibaba Cloud accounts.
        # *   CancelSharing: unshares the template.
        # 
        # This parameter is required.
        self.share_option = share_option
        # The ID of the template.
        # 
        # This parameter is required.
        self.template_id = template_id
        # The version of the shared template. This parameter takes effect only if you set ShareOption to ShareToAccounts and set VersionOption to Specified.
        # 
        # Valid values: v1 to v100.
        self.template_version = template_version
        # The version option for the shared template. This parameter takes effect only if you set ShareOption to ShareToAccounts.
        # 
        # Valid values:
        # 
        # *   AllVersions (default): shares all versions of the template.
        # *   Latest: shares only the latest version of template. When the version of the template is updated, ROS updates the shared version to the latest version.
        # *   Current: shares only the current version of the template. When the version of the template is updated, ROS does not update the shared version.
        # *   Specified: shares only the specified version of the template.
        self.version_option = version_option

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_ids is not None:
            result['AccountIds'] = self.account_ids

        if self.share_option is not None:
            result['ShareOption'] = self.share_option

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version

        if self.version_option is not None:
            result['VersionOption'] = self.version_option

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIds') is not None:
            self.account_ids = m.get('AccountIds')

        if m.get('ShareOption') is not None:
            self.share_option = m.get('ShareOption')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')

        if m.get('VersionOption') is not None:
            self.version_option = m.get('VersionOption')

        return self

