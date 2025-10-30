# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHadoopDataSourceResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        data_source_description: str = None,
        data_source_dir: str = None,
        data_source_id: str = None,
        data_source_name: str = None,
        data_source_status: str = None,
        data_source_type: str = None,
        emr_instance_id: str = None,
        external_data_service_id: str = None,
        hdfsconf: str = None,
        hadoop_core_conf: str = None,
        hadoop_create_type: str = None,
        hadoop_hosts_address: str = None,
        hive_conf: str = None,
        map_reduce_conf: str = None,
        modify_time: str = None,
        request_id: str = None,
        status_message: str = None,
        yarn_conf: str = None,
    ):
        # The time when the service was created.
        self.create_time = create_time
        # The description of the service. The description can be up to 256 characters in length.
        self.data_source_description = data_source_description
        # The service directory in which Hadoop-related configuration files are stored.
        self.data_source_dir = data_source_dir
        # The data source ID.
        self.data_source_id = data_source_id
        # The name of the service.
        self.data_source_name = data_source_name
        # The status of the service. Valid values:
        # 
        # *   Init
        # *   Running
        # *   Exception
        self.data_source_status = data_source_status
        # The type of the data source.
        self.data_source_type = data_source_type
        # The E-MapReduce (EMR) Hadoop cluster ID.
        self.emr_instance_id = emr_instance_id
        # The ID of the external data service.
        self.external_data_service_id = external_data_service_id
        # The content of the Hadoop hdfs-site.xml file.
        self.hdfsconf = hdfsconf
        # The content of the Hadoop core-site.xml file.
        self.hadoop_core_conf = hadoop_core_conf
        # The type of the external service. Valid values:
        # 
        # *   emr
        # *   selfCreate
        self.hadoop_create_type = hadoop_create_type
        # The IP address and hostname of the Hadoop cluster (data source) in the /etc/hosts file.
        self.hadoop_hosts_address = hadoop_hosts_address
        # The content of the Hadoop hive-site.xml file.
        self.hive_conf = hive_conf
        # The content of the Hadoop mapred-site.xml file.
        self.map_reduce_conf = map_reduce_conf
        # The time when the data source was last modified.
        self.modify_time = modify_time
        # The request ID.
        self.request_id = request_id
        # The information about the service status. For example, if the service is in the exception state, the cause of the exception is displayed. If the service is in the running state, this parameter is left empty.
        self.status_message = status_message
        # The content of the Hadoop yarn-site.xml file.
        self.yarn_conf = yarn_conf

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data_source_description is not None:
            result['DataSourceDescription'] = self.data_source_description

        if self.data_source_dir is not None:
            result['DataSourceDir'] = self.data_source_dir

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name

        if self.data_source_status is not None:
            result['DataSourceStatus'] = self.data_source_status

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.emr_instance_id is not None:
            result['EmrInstanceId'] = self.emr_instance_id

        if self.external_data_service_id is not None:
            result['ExternalDataServiceId'] = self.external_data_service_id

        if self.hdfsconf is not None:
            result['HDFSConf'] = self.hdfsconf

        if self.hadoop_core_conf is not None:
            result['HadoopCoreConf'] = self.hadoop_core_conf

        if self.hadoop_create_type is not None:
            result['HadoopCreateType'] = self.hadoop_create_type

        if self.hadoop_hosts_address is not None:
            result['HadoopHostsAddress'] = self.hadoop_hosts_address

        if self.hive_conf is not None:
            result['HiveConf'] = self.hive_conf

        if self.map_reduce_conf is not None:
            result['MapReduceConf'] = self.map_reduce_conf

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status_message is not None:
            result['StatusMessage'] = self.status_message

        if self.yarn_conf is not None:
            result['YarnConf'] = self.yarn_conf

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataSourceDescription') is not None:
            self.data_source_description = m.get('DataSourceDescription')

        if m.get('DataSourceDir') is not None:
            self.data_source_dir = m.get('DataSourceDir')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')

        if m.get('DataSourceStatus') is not None:
            self.data_source_status = m.get('DataSourceStatus')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('EmrInstanceId') is not None:
            self.emr_instance_id = m.get('EmrInstanceId')

        if m.get('ExternalDataServiceId') is not None:
            self.external_data_service_id = m.get('ExternalDataServiceId')

        if m.get('HDFSConf') is not None:
            self.hdfsconf = m.get('HDFSConf')

        if m.get('HadoopCoreConf') is not None:
            self.hadoop_core_conf = m.get('HadoopCoreConf')

        if m.get('HadoopCreateType') is not None:
            self.hadoop_create_type = m.get('HadoopCreateType')

        if m.get('HadoopHostsAddress') is not None:
            self.hadoop_hosts_address = m.get('HadoopHostsAddress')

        if m.get('HiveConf') is not None:
            self.hive_conf = m.get('HiveConf')

        if m.get('MapReduceConf') is not None:
            self.map_reduce_conf = m.get('MapReduceConf')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')

        if m.get('YarnConf') is not None:
            self.yarn_conf = m.get('YarnConf')

        return self

