# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListScriptsRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        script_id: str = None,
        script_name: str = None,
        script_type: str = None,
        statuses: List[str] = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The maximum number of entries to return on each page.
        self.max_results = max_results
        # The token that marks the position from which to start reading.
        self.next_token = next_token
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the cluster script. This parameter is valid only for NORMAL scripts.
        self.script_id = script_id
        # The name of the cluster script. This parameter is valid only for NORMAL scripts and supports fuzzy search.
        self.script_name = script_name
        # The type of the cluster script. Valid values:
        # 
        # - BOOTSTRAP: a bootstrap script.
        # 
        # - NORMAL: a normal cluster script.
        # 
        # This parameter is required.
        self.script_type = script_type
        # The list of script statuses.
        self.statuses = statuses

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.script_name is not None:
            result['ScriptName'] = self.script_name

        if self.script_type is not None:
            result['ScriptType'] = self.script_type

        if self.statuses is not None:
            result['Statuses'] = self.statuses

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('ScriptName') is not None:
            self.script_name = m.get('ScriptName')

        if m.get('ScriptType') is not None:
            self.script_type = m.get('ScriptType')

        if m.get('Statuses') is not None:
            self.statuses = m.get('Statuses')

        return self

