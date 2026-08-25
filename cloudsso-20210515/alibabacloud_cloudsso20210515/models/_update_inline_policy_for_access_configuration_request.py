# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateInlinePolicyForAccessConfigurationRequest(DaraModel):
    def __init__(
        self,
        access_configuration_id: str = None,
        directory_id: str = None,
        inline_policy_name: str = None,
        new_inline_policy_document: str = None,
    ):
        # The ID of the access configuration.
        self.access_configuration_id = access_configuration_id
        # The ID of the directory.
        self.directory_id = directory_id
        # The name of the inline policy.
        self.inline_policy_name = inline_policy_name
        # The new configurations of the inline policy.
        # 
        # The value can be up to 4,096 characters in length.
        # 
        # For more information about the syntax and structure of RAM policies, see [Policy syntax and structure](https://help.aliyun.com/document_detail/93739.html).
        self.new_inline_policy_document = new_inline_policy_document

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_configuration_id is not None:
            result['AccessConfigurationId'] = self.access_configuration_id

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.inline_policy_name is not None:
            result['InlinePolicyName'] = self.inline_policy_name

        if self.new_inline_policy_document is not None:
            result['NewInlinePolicyDocument'] = self.new_inline_policy_document

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessConfigurationId') is not None:
            self.access_configuration_id = m.get('AccessConfigurationId')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('InlinePolicyName') is not None:
            self.inline_policy_name = m.get('InlinePolicyName')

        if m.get('NewInlinePolicyDocument') is not None:
            self.new_inline_policy_document = m.get('NewInlinePolicyDocument')

        return self

