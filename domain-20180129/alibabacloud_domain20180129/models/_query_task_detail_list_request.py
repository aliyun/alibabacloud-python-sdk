# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryTaskDetailListRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        instance_id: str = None,
        lang: str = None,
        page_num: int = None,
        page_size: int = None,
        task_no: str = None,
        task_status: int = None,
        user_client_ip: str = None,
    ):
        # The domain name.
        self.domain_name = domain_name
        # The domain name instance ID.
        # 
        # > You can call <props="china">[QueryDomainByDomainName](https://help.aliyun.com/document_detail/442021.html)<props="intl">[QueryDomainByDomainName](https://help.aliyun.com/document_detail/121704.html) to query the domain name instance ID.
        self.instance_id = instance_id
        # The language of the error message returned by the operation. Valid values:
        # - **zh**: Chinese.
        # - **en**: English.
        # 
        # Default value: **en**.
        self.lang = lang
        # The page number.
        # 
        # This parameter is required.
        self.page_num = page_num
        # The number of entries per page. Maximum value: **1000**.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The task number. This is the TaskNo value returned by a successfully executed task.
        # 
        # This parameter is required.
        self.task_no = task_no
        # The task status. Valid values:
        # - **0**: Waiting to be executed.
        # - **1**: Executing.
        # - **2**: Successful.
        # - **3**: Failed.
        self.task_status = task_status
        # The user IP address. You can set this parameter to **127.0.0.1**.
        self.user_client_ip = user_client_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.task_no is not None:
            result['TaskNo'] = self.task_no

        if self.task_status is not None:
            result['TaskStatus'] = self.task_status

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TaskNo') is not None:
            self.task_no = m.get('TaskNo')

        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

