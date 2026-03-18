# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListJobInfosRequest(DaraModel):
    def __init__(
        self,
        asc_order: bool = None,
        ext_node_id_list: List[str] = None,
        ext_node_name_list: List[str] = None,
        from_: int = None,
        instance_id_list: List[str] = None,
        job_owner_list: List[str] = None,
        priority_list: List[int] = None,
        project_list: List[str] = None,
        quota_nickname: str = None,
        scene_tag_list: List[str] = None,
        signature_list: List[str] = None,
        sort_by_list: List[str] = None,
        sort_order_list: List[str] = None,
        status_list: List[str] = None,
        task_name_list: List[str] = None,
        to: int = None,
        type_list: List[str] = None,
        order_column: str = None,
        page_number: int = None,
        page_size: int = None,
        region: str = None,
        tenant_id: str = None,
    ):
        # Specifies whether to sort the results in ascending or descending order.
        self.asc_order = asc_order
        # The upstream node ID.
        self.ext_node_id_list = ext_node_id_list
        self.ext_node_name_list = ext_node_name_list
        # The start UNIX timestamp.
        # 
        # This parameter is required.
        self.from_ = from_
        # The job instance ID.
        self.instance_id_list = instance_id_list
        # The job owner.
        self.job_owner_list = job_owner_list
        # The job priority.
        self.priority_list = priority_list
        # The project name.
        self.project_list = project_list
        # The nickname of the quota.
        self.quota_nickname = quota_nickname
        # The smart diagnosis tag.
        self.scene_tag_list = scene_tag_list
        # The job signature.
        self.signature_list = signature_list
        # The fields for multi-column sorting.
        self.sort_by_list = sort_by_list
        # The sort orders for multi-column sorting.
        self.sort_order_list = sort_order_list
        # The job status.
        self.status_list = status_list
        self.task_name_list = task_name_list
        # The end UNIX timestamp.
        # 
        # This parameter is required.
        self.to = to
        # The job type.
        self.type_list = type_list
        # The column to use for sorting.
        self.order_column = order_column
        # The page number.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # The region ID.
        self.region = region
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asc_order is not None:
            result['ascOrder'] = self.asc_order

        if self.ext_node_id_list is not None:
            result['extNodeIdList'] = self.ext_node_id_list

        if self.ext_node_name_list is not None:
            result['extNodeNameList'] = self.ext_node_name_list

        if self.from_ is not None:
            result['from'] = self.from_

        if self.instance_id_list is not None:
            result['instanceIdList'] = self.instance_id_list

        if self.job_owner_list is not None:
            result['jobOwnerList'] = self.job_owner_list

        if self.priority_list is not None:
            result['priorityList'] = self.priority_list

        if self.project_list is not None:
            result['projectList'] = self.project_list

        if self.quota_nickname is not None:
            result['quotaNickname'] = self.quota_nickname

        if self.scene_tag_list is not None:
            result['sceneTagList'] = self.scene_tag_list

        if self.signature_list is not None:
            result['signatureList'] = self.signature_list

        if self.sort_by_list is not None:
            result['sortByList'] = self.sort_by_list

        if self.sort_order_list is not None:
            result['sortOrderList'] = self.sort_order_list

        if self.status_list is not None:
            result['statusList'] = self.status_list

        if self.task_name_list is not None:
            result['taskNameList'] = self.task_name_list

        if self.to is not None:
            result['to'] = self.to

        if self.type_list is not None:
            result['typeList'] = self.type_list

        if self.order_column is not None:
            result['orderColumn'] = self.order_column

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.region is not None:
            result['region'] = self.region

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ascOrder') is not None:
            self.asc_order = m.get('ascOrder')

        if m.get('extNodeIdList') is not None:
            self.ext_node_id_list = m.get('extNodeIdList')

        if m.get('extNodeNameList') is not None:
            self.ext_node_name_list = m.get('extNodeNameList')

        if m.get('from') is not None:
            self.from_ = m.get('from')

        if m.get('instanceIdList') is not None:
            self.instance_id_list = m.get('instanceIdList')

        if m.get('jobOwnerList') is not None:
            self.job_owner_list = m.get('jobOwnerList')

        if m.get('priorityList') is not None:
            self.priority_list = m.get('priorityList')

        if m.get('projectList') is not None:
            self.project_list = m.get('projectList')

        if m.get('quotaNickname') is not None:
            self.quota_nickname = m.get('quotaNickname')

        if m.get('sceneTagList') is not None:
            self.scene_tag_list = m.get('sceneTagList')

        if m.get('signatureList') is not None:
            self.signature_list = m.get('signatureList')

        if m.get('sortByList') is not None:
            self.sort_by_list = m.get('sortByList')

        if m.get('sortOrderList') is not None:
            self.sort_order_list = m.get('sortOrderList')

        if m.get('statusList') is not None:
            self.status_list = m.get('statusList')

        if m.get('taskNameList') is not None:
            self.task_name_list = m.get('taskNameList')

        if m.get('to') is not None:
            self.to = m.get('to')

        if m.get('typeList') is not None:
            self.type_list = m.get('typeList')

        if m.get('orderColumn') is not None:
            self.order_column = m.get('orderColumn')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

