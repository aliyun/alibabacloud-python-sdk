# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class ListMmsDataSourcesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListMmsDataSourcesResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The request ID.
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
            temp_model = main_models.ListMmsDataSourcesResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListMmsDataSourcesResponseBodyData(DaraModel):
    def __init__(
        self,
        object_list: List[main_models.ListMmsDataSourcesResponseBodyDataObjectList] = None,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # The list of data sources.
        self.object_list = object_list
        # The page number.
        self.page_num = page_num
        # The number of entries per page.
        self.page_size = page_size
        # The total number of records.
        self.total = total

    def validate(self):
        if self.object_list:
            for v1 in self.object_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['objectList'] = []
        if self.object_list is not None:
            for k1 in self.object_list:
                result['objectList'].append(k1.to_map() if k1 else None)

        if self.page_num is not None:
            result['pageNum'] = self.page_num

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.object_list = []
        if m.get('objectList') is not None:
            for k1 in m.get('objectList'):
                temp_model = main_models.ListMmsDataSourcesResponseBodyDataObjectList()
                self.object_list.append(temp_model.from_map(k1))

        if m.get('pageNum') is not None:
            self.page_num = m.get('pageNum')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListMmsDataSourcesResponseBodyDataObjectList(DaraModel):
    def __init__(
        self,
        agent_is_online: bool = None,
        config: List[main_models.ListMmsDataSourcesResponseBodyDataObjectListConfig] = None,
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
        # Indicates whether the data source instance or its associated agent is started.
        self.agent_is_online = agent_is_online
        # The configurations of the data source.
        self.config = config
        # The time when the data source was created.
        self.create_time = create_time
        # The number of databases in the data source.
        self.db_num = db_num
        # The default destination MaxCompute project.
        self.dst_project = dst_project
        # The list of destination MaxCompute projects.
        self.dst_projects = dst_projects
        # The reason why the data source instance failed to start or shut down. This parameter is returned only when the value of \\`status\\` is \\`START_FAILED\\` or \\`STOP_FAILED\\`.
        self.err_msg = err_msg
        # The data source ID.
        self.id = id
        # The last time when the metadata was synchronized.
        self.last_update_time = last_update_time
        # The name of the data source.
        self.name = name
        # The MaxCompute network connectivity ID is the region ID.
        self.networklink = networklink
        # The number of partitions in the data source.
        self.partition_num = partition_num
        # The number of partitions that are being migrated.
        self.partitions_doing_num = partitions_doing_num
        # The number of partitions that have been migrated.
        self.partitions_done_num = partitions_done_num
        # The number of partitions that failed to be migrated.
        self.partitions_failed_num = partitions_failed_num
        # The region ID.
        self.region = region
        # The ID of the metadata synchronization task.
        self.scan_id = scan_id
        # The status of the data source.
        self.status = status
        # The number of tables in the data source.
        self.table_num = table_num
        # The number of tables that are being migrated.
        self.tables_doing_num = tables_doing_num
        # The number of tables that have been migrated.
        self.tables_done_num = tables_done_num
        # The number of tables that failed to be migrated.
        self.tables_failed_num = tables_failed_num
        # The number of tables that are partially migrated.
        self.tables_part_done_num = tables_part_done_num
        # The type of the data source.
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
                temp_model = main_models.ListMmsDataSourcesResponseBodyDataObjectListConfig()
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

class ListMmsDataSourcesResponseBodyDataObjectListConfig(DaraModel):
    def __init__(
        self,
        desc: str = None,
        enums: List[str] = None,
        group: str = None,
        key: str = None,
        name: str = None,
        place_holder: str = None,
        required: bool = None,
        sub_type: str = None,
        type: str = None,
        value: Any = None,
    ):
        # The description of the configuration.
        self.desc = desc
        # The enumerated values for the configuration.
        self.enums = enums
        # The configuration group.
        self.group = group
        # The English identifier for the configuration.
        self.key = key
        # The name of the configuration.
        self.name = name
        # An example value for the configuration.
        self.place_holder = place_holder
        # Indicates whether the configuration is required.
        self.required = required
        # If \\`type\\` is set to \\`file\\`, \\`subType\\` specifies the file type, such as \\`.keytab\\`.
        self.sub_type = sub_type
        # The type of the configuration. Valid values: \\`boolean\\`, \\`int\\`, \\`map\\`, \\`string\\`, \\`password\\`, and \\`file\\`.
        self.type = type
        # The value of the configuration.
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

        if m.get('subType') is not None:
            self.sub_type = m.get('subType')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

