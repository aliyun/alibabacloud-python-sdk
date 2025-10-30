# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateHadoopDataSourceRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        data_source_description: str = None,
        data_source_name: str = None,
        data_source_type: str = None,
        emr_instance_id: str = None,
        hdfsconf: str = None,
        hadoop_core_conf: str = None,
        hadoop_create_type: str = None,
        hadoop_hosts_address: str = None,
        hive_conf: str = None,
        map_reduce_conf: str = None,
        region_id: str = None,
        yarn_conf: str = None,
    ):
        # Instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # Service description.
        self.data_source_description = data_source_description
        # Service name.
        self.data_source_name = data_source_name
        # Type of Hadoop external table to be enabled, with values:
        # 
        # - HDFS 
        # 
        # - Hive
        self.data_source_type = data_source_type
        # When HadoopCreateType=Emr, this field should contain the EMR instance ID.
        self.emr_instance_id = emr_instance_id
        # Content string of the Hadoop hdfs-site.xml file. This field is required when enabling an HDFS external table.
        self.hdfsconf = hdfsconf
        # Content string of the Hadoop core-site.xml file.
        self.hadoop_core_conf = hadoop_core_conf
        # External service type:
        # 
        # - emr
        # 
        # - hadoop: Self-built Hadoop
        self.hadoop_create_type = hadoop_create_type
        # Address and hostname of the Hadoop cluster\\"s source node in the /etc/hosts file.
        self.hadoop_hosts_address = hadoop_hosts_address
        # Content string of the Hadoop hive-site.xml file. This field is required when enabling a HIVE external table.
        self.hive_conf = hive_conf
        # Content string of the Hadoop mapred-site.xml file. This field is required when enabling an HDFS external table.
        self.map_reduce_conf = map_reduce_conf
        # Region ID.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/86912.html) interface to view available region IDs.
        self.region_id = region_id
        # Content string of the Hadoop yarn-site.xml file. This field is required when enabling an HDFS external table.
        self.yarn_conf = yarn_conf

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.data_source_description is not None:
            result['DataSourceDescription'] = self.data_source_description

        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.emr_instance_id is not None:
            result['EmrInstanceId'] = self.emr_instance_id

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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.yarn_conf is not None:
            result['YarnConf'] = self.yarn_conf

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DataSourceDescription') is not None:
            self.data_source_description = m.get('DataSourceDescription')

        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('EmrInstanceId') is not None:
            self.emr_instance_id = m.get('EmrInstanceId')

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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('YarnConf') is not None:
            self.yarn_conf = m.get('YarnConf')

        return self

