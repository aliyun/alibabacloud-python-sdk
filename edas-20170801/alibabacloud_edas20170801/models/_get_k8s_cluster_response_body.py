# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class GetK8sClusterResponseBody(DaraModel):
    def __init__(
        self,
        cluster_page: main_models.GetK8sClusterResponseBodyClusterPage = None,
        code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        # The paginated list of clusters.
        self.cluster_page = cluster_page
        # The status of the call or a POP error code.
        self.code = code
        # The additional information.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.cluster_page:
            self.cluster_page.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_page is not None:
            result['ClusterPage'] = self.cluster_page.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterPage') is not None:
            temp_model = main_models.GetK8sClusterResponseBodyClusterPage()
            self.cluster_page = temp_model.from_map(m.get('ClusterPage'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetK8sClusterResponseBodyClusterPage(DaraModel):
    def __init__(
        self,
        cluster_list: main_models.GetK8sClusterResponseBodyClusterPageClusterList = None,
        current_page: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        self.cluster_list = cluster_list
        # The number of the returned page. The default value is 1.
        self.current_page = current_page
        # The number of entries returned per page. The default value is 1000.
        self.page_size = page_size
        # The total number of pages.
        self.total_size = total_size

    def validate(self):
        if self.cluster_list:
            self.cluster_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_list is not None:
            result['ClusterList'] = self.cluster_list.to_map()

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterList') is not None:
            temp_model = main_models.GetK8sClusterResponseBodyClusterPageClusterList()
            self.cluster_list = temp_model.from_map(m.get('ClusterList'))

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class GetK8sClusterResponseBodyClusterPageClusterList(DaraModel):
    def __init__(
        self,
        cluster: List[main_models.GetK8sClusterResponseBodyClusterPageClusterListCluster] = None,
    ):
        self.cluster = cluster

    def validate(self):
        if self.cluster:
            for v1 in self.cluster:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Cluster'] = []
        if self.cluster is not None:
            for k1 in self.cluster:
                result['Cluster'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cluster = []
        if m.get('Cluster') is not None:
            for k1 in m.get('Cluster'):
                temp_model = main_models.GetK8sClusterResponseBodyClusterPageClusterListCluster()
                self.cluster.append(temp_model.from_map(k1))

        return self

class GetK8sClusterResponseBodyClusterPageClusterListCluster(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_import_status: int = None,
        cluster_name: str = None,
        cluster_status: int = None,
        cluster_type: int = None,
        cpu: int = None,
        cs_cluster_id: str = None,
        cs_cluster_status: str = None,
        description: str = None,
        mem: int = None,
        network_mode: int = None,
        node_num: int = None,
        region_id: str = None,
        sub_cluster_type: str = None,
        sub_net_cidr: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_import_status = cluster_import_status
        self.cluster_name = cluster_name
        self.cluster_status = cluster_status
        self.cluster_type = cluster_type
        self.cpu = cpu
        self.cs_cluster_id = cs_cluster_id
        self.cs_cluster_status = cs_cluster_status
        self.description = description
        self.mem = mem
        self.network_mode = network_mode
        self.node_num = node_num
        self.region_id = region_id
        self.sub_cluster_type = sub_cluster_type
        self.sub_net_cidr = sub_net_cidr
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_import_status is not None:
            result['ClusterImportStatus'] = self.cluster_import_status

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cluster_status is not None:
            result['ClusterStatus'] = self.cluster_status

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.cs_cluster_id is not None:
            result['CsClusterId'] = self.cs_cluster_id

        if self.cs_cluster_status is not None:
            result['CsClusterStatus'] = self.cs_cluster_status

        if self.description is not None:
            result['Description'] = self.description

        if self.mem is not None:
            result['Mem'] = self.mem

        if self.network_mode is not None:
            result['NetworkMode'] = self.network_mode

        if self.node_num is not None:
            result['NodeNum'] = self.node_num

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sub_cluster_type is not None:
            result['SubClusterType'] = self.sub_cluster_type

        if self.sub_net_cidr is not None:
            result['SubNetCidr'] = self.sub_net_cidr

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterImportStatus') is not None:
            self.cluster_import_status = m.get('ClusterImportStatus')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterStatus') is not None:
            self.cluster_status = m.get('ClusterStatus')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('CsClusterId') is not None:
            self.cs_cluster_id = m.get('CsClusterId')

        if m.get('CsClusterStatus') is not None:
            self.cs_cluster_status = m.get('CsClusterStatus')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Mem') is not None:
            self.mem = m.get('Mem')

        if m.get('NetworkMode') is not None:
            self.network_mode = m.get('NetworkMode')

        if m.get('NodeNum') is not None:
            self.node_num = m.get('NodeNum')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SubClusterType') is not None:
            self.sub_cluster_type = m.get('SubClusterType')

        if m.get('SubNetCidr') is not None:
            self.sub_net_cidr = m.get('SubNetCidr')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        return self

