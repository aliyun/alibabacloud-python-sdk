# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeEvaluateAndImportTasksResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeEvaluateAndImportTasksResponseBodyData] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_number: int = None,
    ):
        self.data = data
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_number = total_number

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_number is not None:
            result['TotalNumber'] = self.total_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeEvaluateAndImportTasksResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalNumber') is not None:
            self.total_number = m.get('TotalNumber')

        return self

class DescribeEvaluateAndImportTasksResponseBodyData(DaraModel):
    def __init__(
        self,
        bid: str = None,
        creator: str = None,
        deleted: bool = None,
        gmt_created: int = None,
        gmt_modified: int = None,
        id: int = None,
        region_id: str = None,
        slink_dst_db: str = None,
        slink_dst_res_id: str = None,
        slink_dst_user_name: str = None,
        slink_src_db: str = None,
        slink_src_res_id: str = None,
        slink_src_res_type: str = None,
        slink_src_user_name: str = None,
        slink_stage: str = None,
        slink_status: str = None,
        slink_task_desc: str = None,
        slink_task_id: str = None,
        slink_type: str = None,
    ):
        self.bid = bid
        self.creator = creator
        self.deleted = deleted
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        self.id = id
        self.region_id = region_id
        self.slink_dst_db = slink_dst_db
        self.slink_dst_res_id = slink_dst_res_id
        self.slink_dst_user_name = slink_dst_user_name
        self.slink_src_db = slink_src_db
        self.slink_src_res_id = slink_src_res_id
        self.slink_src_res_type = slink_src_res_type
        self.slink_src_user_name = slink_src_user_name
        self.slink_stage = slink_stage
        self.slink_status = slink_status
        self.slink_task_desc = slink_task_desc
        self.slink_task_id = slink_task_id
        self.slink_type = slink_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bid is not None:
            result['Bid'] = self.bid

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.deleted is not None:
            result['Deleted'] = self.deleted

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.slink_dst_db is not None:
            result['SlinkDstDb'] = self.slink_dst_db

        if self.slink_dst_res_id is not None:
            result['SlinkDstResId'] = self.slink_dst_res_id

        if self.slink_dst_user_name is not None:
            result['SlinkDstUserName'] = self.slink_dst_user_name

        if self.slink_src_db is not None:
            result['SlinkSrcDb'] = self.slink_src_db

        if self.slink_src_res_id is not None:
            result['SlinkSrcResId'] = self.slink_src_res_id

        if self.slink_src_res_type is not None:
            result['SlinkSrcResType'] = self.slink_src_res_type

        if self.slink_src_user_name is not None:
            result['SlinkSrcUserName'] = self.slink_src_user_name

        if self.slink_stage is not None:
            result['SlinkStage'] = self.slink_stage

        if self.slink_status is not None:
            result['SlinkStatus'] = self.slink_status

        if self.slink_task_desc is not None:
            result['SlinkTaskDesc'] = self.slink_task_desc

        if self.slink_task_id is not None:
            result['SlinkTaskId'] = self.slink_task_id

        if self.slink_type is not None:
            result['SlinkType'] = self.slink_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SlinkDstDb') is not None:
            self.slink_dst_db = m.get('SlinkDstDb')

        if m.get('SlinkDstResId') is not None:
            self.slink_dst_res_id = m.get('SlinkDstResId')

        if m.get('SlinkDstUserName') is not None:
            self.slink_dst_user_name = m.get('SlinkDstUserName')

        if m.get('SlinkSrcDb') is not None:
            self.slink_src_db = m.get('SlinkSrcDb')

        if m.get('SlinkSrcResId') is not None:
            self.slink_src_res_id = m.get('SlinkSrcResId')

        if m.get('SlinkSrcResType') is not None:
            self.slink_src_res_type = m.get('SlinkSrcResType')

        if m.get('SlinkSrcUserName') is not None:
            self.slink_src_user_name = m.get('SlinkSrcUserName')

        if m.get('SlinkStage') is not None:
            self.slink_stage = m.get('SlinkStage')

        if m.get('SlinkStatus') is not None:
            self.slink_status = m.get('SlinkStatus')

        if m.get('SlinkTaskDesc') is not None:
            self.slink_task_desc = m.get('SlinkTaskDesc')

        if m.get('SlinkTaskId') is not None:
            self.slink_task_id = m.get('SlinkTaskId')

        if m.get('SlinkType') is not None:
            self.slink_type = m.get('SlinkType')

        return self

