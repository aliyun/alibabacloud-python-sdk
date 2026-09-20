# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateNamespaceRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        namespace_id: str = None,
        scan_policy: str = None,
        tags: str = None,
    ):
        # The workspace description.
        self.description = description
        # The workspace name.
        self.name = name
        # The workspace ID.
        # 
        # This parameter is required.
        self.namespace_id = namespace_id
        # The scan policy.
        # 
        # The policy contains two configuration items:
        # - minBlockRiskLevel: the risk level for blocking.
        #   - high: blocks high-risk items.
        #   - medium: blocks medium-risk and high-risk items.
        #   - low: blocks all risk levels including high, medium, and low.
        # - maxSkipRatio: the max false positive rate. If the scan skip ratio exceeds this value, the scan is considered failed.
        self.scan_policy = scan_policy
        # The tags, separated by commas. Pass an empty string to clear all tags.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.scan_policy is not None:
            result['ScanPolicy'] = self.scan_policy

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('ScanPolicy') is not None:
            self.scan_policy = m.get('ScanPolicy')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

