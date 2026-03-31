# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class GetMmsDataSourceResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetMmsDataSourceResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetMmsDataSourceResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetMmsDataSourceResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_is_online: bool = None,
        config: List[main_models.GetMmsDataSourceResponseBodyDataConfig] = None,
        create_time: str = None,
        db_num: int = None,
        dst_project: str = None,
        dst_projects: List[str] = None,
        err_msg: str = None,
        id: int = None,
        last_update_time: str = None,
        name: str = None,
        networklink: str = None,
        partition_num: int = None,
        partitions_doing_num: int = None,
        partitions_done_num: int = None,
        partitions_failed_num: int = None,
        region: str = None,
        scan_id: int = None,
        status: str = None,
        table_num: int = None,
        tables_doing_num: int = None,
        tables_done_num: int = None,
        tables_failed_num: int = None,
        tables_part_done_num: int = None,
        type: str = None,
    ):
        self.agent_is_online = agent_is_online
        self.config = config
        self.create_time = create_time
        self.db_num = db_num
        self.dst_project = dst_project
        self.dst_projects = dst_projects
        self.err_msg = err_msg
        self.id = id
        self.last_update_time = last_update_time
        self.name = name
        self.networklink = networklink
        self.partition_num = partition_num
        self.partitions_doing_num = partitions_doing_num
        self.partitions_done_num = partitions_done_num
        self.partitions_failed_num = partitions_failed_num
        self.region = region
        self.scan_id = scan_id
        self.status = status
        self.table_num = table_num
        self.tables_doing_num = tables_doing_num
        self.tables_done_num = tables_done_num
        self.tables_failed_num = tables_failed_num
        self.tables_part_done_num = tables_part_done_num
        self.type = type

    def validate(self):
        if self.config:
            for v1 in self.config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_is_online is not None:
            result['agentIsOnline'] = self.agent_is_online

        result['config'] = []
        if self.config is not None:
            for k1 in self.config:
                result['config'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.db_num is not None:
            result['dbNum'] = self.db_num

        if self.dst_project is not None:
            result['dstProject'] = self.dst_project

        if self.dst_projects is not None:
            result['dstProjects'] = self.dst_projects

        if self.err_msg is not None:
            result['errMsg'] = self.err_msg

        if self.id is not None:
            result['id'] = self.id

        if self.last_update_time is not None:
            result['lastUpdateTime'] = self.last_update_time

        if self.name is not None:
            result['name'] = self.name

        if self.networklink is not None:
            result['networklink'] = self.networklink

        if self.partition_num is not None:
            result['partitionNum'] = self.partition_num

        if self.partitions_doing_num is not None:
            result['partitionsDoingNum'] = self.partitions_doing_num

        if self.partitions_done_num is not None:
            result['partitionsDoneNum'] = self.partitions_done_num

        if self.partitions_failed_num is not None:
            result['partitionsFailedNum'] = self.partitions_failed_num

        if self.region is not None:
            result['region'] = self.region

        if self.scan_id is not None:
            result['scanId'] = self.scan_id

        if self.status is not None:
            result['status'] = self.status

        if self.table_num is not None:
            result['tableNum'] = self.table_num

        if self.tables_doing_num is not None:
            result['tablesDoingNum'] = self.tables_doing_num

        if self.tables_done_num is not None:
            result['tablesDoneNum'] = self.tables_done_num

        if self.tables_failed_num is not None:
            result['tablesFailedNum'] = self.tables_failed_num

        if self.tables_part_done_num is not None:
            result['tablesPartDoneNum'] = self.tables_part_done_num

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentIsOnline') is not None:
            self.agent_is_online = m.get('agentIsOnline')

        self.config = []
        if m.get('config') is not None:
            for k1 in m.get('config'):
                temp_model = main_models.GetMmsDataSourceResponseBodyDataConfig()
                self.config.append(temp_model.from_map(k1))

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('dbNum') is not None:
            self.db_num = m.get('dbNum')

        if m.get('dstProject') is not None:
            self.dst_project = m.get('dstProject')

        if m.get('dstProjects') is not None:
            self.dst_projects = m.get('dstProjects')

        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('lastUpdateTime') is not None:
            self.last_update_time = m.get('lastUpdateTime')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('networklink') is not None:
            self.networklink = m.get('networklink')

        if m.get('partitionNum') is not None:
            self.partition_num = m.get('partitionNum')

        if m.get('partitionsDoingNum') is not None:
            self.partitions_doing_num = m.get('partitionsDoingNum')

        if m.get('partitionsDoneNum') is not None:
            self.partitions_done_num = m.get('partitionsDoneNum')

        if m.get('partitionsFailedNum') is not None:
            self.partitions_failed_num = m.get('partitionsFailedNum')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('scanId') is not None:
            self.scan_id = m.get('scanId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('tableNum') is not None:
            self.table_num = m.get('tableNum')

        if m.get('tablesDoingNum') is not None:
            self.tables_doing_num = m.get('tablesDoingNum')

        if m.get('tablesDoneNum') is not None:
            self.tables_done_num = m.get('tablesDoneNum')

        if m.get('tablesFailedNum') is not None:
            self.tables_failed_num = m.get('tablesFailedNum')

        if m.get('tablesPartDoneNum') is not None:
            self.tables_part_done_num = m.get('tablesPartDoneNum')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class GetMmsDataSourceResponseBodyDataConfig(DaraModel):
    def __init__(
        self,
        desc: str = None,
        enums: List[str] = None,
        group: str = None,
        key: str = None,
        name: str = None,
        place_holder: str = None,
        required: bool = None,
        sub_items: Dict[str, Any] = None,
        sub_type: str = None,
        type: str = None,
        value: Any = None,
    ):
        self.desc = desc
        self.enums = enums
        self.group = group
        self.key = key
        self.name = name
        self.place_holder = place_holder
        self.required = required
        self.sub_items = sub_items
        self.sub_type = sub_type
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['desc'] = self.desc

        if self.enums is not None:
            result['enums'] = self.enums

        if self.group is not None:
            result['group'] = self.group

        if self.key is not None:
            result['key'] = self.key

        if self.name is not None:
            result['name'] = self.name

        if self.place_holder is not None:
            result['placeHolder'] = self.place_holder

        if self.required is not None:
            result['required'] = self.required

        if self.sub_items is not None:
            result['subItems'] = self.sub_items

        if self.sub_type is not None:
            result['subType'] = self.sub_type

        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')

        if m.get('enums') is not None:
            self.enums = m.get('enums')

        if m.get('group') is not None:
            self.group = m.get('group')

        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('placeHolder') is not None:
            self.place_holder = m.get('placeHolder')

        if m.get('required') is not None:
            self.required = m.get('required')

        if m.get('subItems') is not None:
            self.sub_items = m.get('subItems')

        if m.get('subType') is not None:
            self.sub_type = m.get('subType')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

