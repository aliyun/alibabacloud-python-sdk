# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEventCenterRecordRequest(DaraModel):
    def __init__(
        self,
        event_type: str = None,
        instance_id: str = None,
        page_no: int = None,
        page_size: int = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
        rule_id: str = None,
    ):
        # The type of the event. Valid values:
        # 
        # *   `cr:Artifact:DeliveryChainCompleted`: The delivery chain is processed.
        # *   `cr:Artifact:SynchronizationCompleted`: The image is replicated.
        # *   `cr:Artifact:BuildCompleted`: The image is built.
        # *   `cr:Artifact:ScanCompleted`: The image is scanned.
        # *   `cr:Artifact:SigningCompleted`: The image is signed.
        self.event_type = event_type
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of the page to return.
        self.page_no = page_no
        # The number of entries to return on each page.
        self.page_size = page_size
        # The name of the repository.
        self.repo_name = repo_name
        # The name of the namespace to which the repository belongs.
        self.repo_namespace_name = repo_namespace_name
        # The ID of the event notification rule.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

