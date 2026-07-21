# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeInvocationsRequest(DaraModel):
    def __init__(
        self,
        command_type: str = None,
        content_encoding: str = None,
        desktop_id: str = None,
        desktop_ids: List[str] = None,
        end_user_id: str = None,
        include_invoke_desktops: bool = None,
        include_output: bool = None,
        invoke_id: str = None,
        invoke_status: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
    ):
        # The command type of the O&M script.
        self.command_type = command_type
        # The encoding method of the returned data.
        self.content_encoding = content_encoding
        # The cloud desktop ID. If you specify a cloud desktop, all script execution records for that cloud desktop are queried.
        self.desktop_id = desktop_id
        # The list of cloud desktop IDs.
        # 
        # > The `DesktopId` parameter will be deprecated. Use this parameter to pass the list of cloud desktop IDs.
        self.desktop_ids = desktop_ids
        # The user ID.
        self.end_user_id = end_user_id
        # Specifies whether to return the execution results of all cloud desktops when a remote command is run on multiple cloud desktops.
        self.include_invoke_desktops = include_invoke_desktops
        # Specifies whether to return the output of the script execution in the results.
        self.include_output = include_output
        # The script execution ID. Obtained from the response of [RunCommand](~~RunCommand~~).
        self.invoke_id = invoke_id
        # The overall execution status of the script. The overall execution status depends on the combined execution status of one or more cloud desktops in the execution.
        self.invoke_status = invoke_status
        # The number of entries per page for a paged query.    
        # 
        # - Maximum value: 50.
        # - Default value: 10.
        self.max_results = max_results
        # The pagination token. Set this parameter to the NextToken value returned in the previous API call.
        self.next_token = next_token
        # The region ID. Call [DescribeRegions](~~DescribeRegions~~) to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command_type is not None:
            result['CommandType'] = self.command_type

        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding

        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.desktop_ids is not None:
            result['DesktopIds'] = self.desktop_ids

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.include_invoke_desktops is not None:
            result['IncludeInvokeDesktops'] = self.include_invoke_desktops

        if self.include_output is not None:
            result['IncludeOutput'] = self.include_output

        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id

        if self.invoke_status is not None:
            result['InvokeStatus'] = self.invoke_status

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandType') is not None:
            self.command_type = m.get('CommandType')

        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')

        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('DesktopIds') is not None:
            self.desktop_ids = m.get('DesktopIds')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('IncludeInvokeDesktops') is not None:
            self.include_invoke_desktops = m.get('IncludeInvokeDesktops')

        if m.get('IncludeOutput') is not None:
            self.include_output = m.get('IncludeOutput')

        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')

        if m.get('InvokeStatus') is not None:
            self.invoke_status = m.get('InvokeStatus')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

