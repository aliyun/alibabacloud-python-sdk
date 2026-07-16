# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCheckWarningDetailRequest(DaraModel):
    def __init__(
        self,
        check_id: str = None,
        check_warning_id: int = None,
        container_name: str = None,
        lang: str = None,
        resource_directory_account_id: int = None,
        source_ip: str = None,
        uuid: str = None,
    ):
        # The ID of the check item.
        # > You can call the [ListCheckItemWarningSummary](~~ListCheckItemWarningSummary~~) operation to obtain the check item ID.>Notice: When this parameter is specified, the Uuid parameter is required..
        self.check_id = check_id
        # The alert ID of the check item.
        # 
        # > To query the details of a specified check item, provide the alert ID of the check item. You can call the [DescribeCheckWarnings](~~DescribeCheckWarnings~~) operation to obtain this ID.
        # >Notice: This parameter is required when both Uuid and CheckId are empty..
        self.check_warning_id = check_warning_id
        # The container name.
        self.container_name = container_name
        # The language of the request and response. Valid values:
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The ID of the Alibaba Cloud account of the member accounts in the resource folder.
        # >You can invoke the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain this parameter.
        self.resource_directory_account_id = resource_directory_account_id
        # The source IP address of the request.
        self.source_ip = source_ip
        # The UUID of the server to query.
        # > You can call the [DescribeCloudCenterInstances](~~DescribeCloudCenterInstances~~) operation to obtain this parameter.>Notice: When this parameter is specified, the CheckId parameter is required..
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.check_warning_id is not None:
            result['CheckWarningId'] = self.check_warning_id

        if self.container_name is not None:
            result['ContainerName'] = self.container_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('CheckWarningId') is not None:
            self.check_warning_id = m.get('CheckWarningId')

        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

