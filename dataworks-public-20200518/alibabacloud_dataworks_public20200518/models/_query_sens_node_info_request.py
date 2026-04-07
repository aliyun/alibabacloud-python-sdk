# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuerySensNodeInfoRequest(DaraModel):
    def __init__(
        self,
        node_id: str = None,
        page_no: int = None,
        page_size: int = None,
        sensitive_name: str = None,
        template_id: str = None,
        tenant_id: str = None,
        status: int = None,
    ):
        # The ID of the data category. You can call the [QuerySensClassification](https://help.aliyun.com/document_detail/2746850.html) operation or log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Data Security Guard page to obtain the ID.
        self.node_id = node_id
        # The page number. Pages start from page 1.
        self.page_no = page_no
        # The number of entries per page. Valid values: 10 to 1000. The recommended number of entries per page ranges from 10 to 100.
        self.page_size = page_size
        # The name of the sensitive field. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Data Security Guard page to obtain the name.
        self.sensitive_name = sensitive_name
        # The ID of the data category and data sensitivity level template. You can call the [QueryDefaultTemplate](https://help.aliyun.com/document_detail/2743948.html) operation to query the ID.
        # 
        # This parameter is required.
        self.template_id = template_id
        # The tenant ID. To obtain the tenant ID, perform the following steps: Log on to the [DataWorks console](https://workbench.data.aliyun.com/console). Find your workspace and go to the DataStudio page. On the DataStudio page, click the logon username in the upper-right corner and click User Info in the Menu section.
        # 
        # This parameter is required.
        self.tenant_id = tenant_id
        # The status of the sensitive field. Valid values:
        # 
        # *   0: draft
        # *   1: published
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sensitive_name is not None:
            result['SensitiveName'] = self.sensitive_name

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SensitiveName') is not None:
            self.sensitive_name = m.get('SensitiveName')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

