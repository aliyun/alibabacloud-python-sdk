# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeNsasSuspEventTypeRequest(DaraModel):
    def __init__(
        self,
        container_field_name: str = None,
        container_field_value: str = None,
        from_: str = None,
        lang: str = None,
        multi_account_action_type: int = None,
        name: str = None,
        remark: str = None,
        source_ip: str = None,
        support_operate_code_list: List[str] = None,
        uuids: str = None,
    ):
        # The container field. Valid values:
        # 
        # - **clusterId**: cluster ID.
        self.container_field_name = container_field_name
        # The value of the container field.
        self.container_field_value = container_field_value
        # The source of the request. Set the value to **sas**, which indicates that the request is sent from Security Center.
        self.from_ = from_
        # The language of the request and response. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The multi-account query type. Default value: **0**. Valid values:
        # - **0**: queries data of the current account.
        # - **1**: queries data of all accounts.
        self.multi_account_action_type = multi_account_action_type
        # The name of the security alerting Alarm Metric.
        self.name = name
        # The name of the server.
        self.remark = remark
        # The IP address of the access source.
        self.source_ip = source_ip
        # The list of operation types supported by the alert.
        self.support_operate_code_list = support_operate_code_list
        # The UUIDs of the servers. Separate multiple UUIDs with commas (,).
        # > Call the [DescribeCloudCenterInstances](https://help.aliyun.com/document_detail/141932.html) operation to obtain this parameter.
        self.uuids = uuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.container_field_name is not None:
            result['ContainerFieldName'] = self.container_field_name

        if self.container_field_value is not None:
            result['ContainerFieldValue'] = self.container_field_value

        if self.from_ is not None:
            result['From'] = self.from_

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.multi_account_action_type is not None:
            result['MultiAccountActionType'] = self.multi_account_action_type

        if self.name is not None:
            result['Name'] = self.name

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.support_operate_code_list is not None:
            result['SupportOperateCodeList'] = self.support_operate_code_list

        if self.uuids is not None:
            result['Uuids'] = self.uuids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerFieldName') is not None:
            self.container_field_name = m.get('ContainerFieldName')

        if m.get('ContainerFieldValue') is not None:
            self.container_field_value = m.get('ContainerFieldValue')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MultiAccountActionType') is not None:
            self.multi_account_action_type = m.get('MultiAccountActionType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('SupportOperateCodeList') is not None:
            self.support_operate_code_list = m.get('SupportOperateCodeList')

        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        return self

