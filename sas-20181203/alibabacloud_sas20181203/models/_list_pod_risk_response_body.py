# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListPodRiskResponseBody(DaraModel):
    def __init__(
        self,
        page_info: main_models.ListPodRiskResponseBodyPageInfo = None,
        pod_risk_list: List[main_models.ListPodRiskResponseBodyPodRiskList] = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.page_info = page_info
        # An array that consists of the risks.
        self.pod_risk_list = pod_risk_list
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.pod_risk_list:
            for v1 in self.pod_risk_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        result['PodRiskList'] = []
        if self.pod_risk_list is not None:
            for k1 in self.pod_risk_list:
                result['PodRiskList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = main_models.ListPodRiskResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        self.pod_risk_list = []
        if m.get('PodRiskList') is not None:
            for k1 in m.get('PodRiskList'):
                temp_model = main_models.ListPodRiskResponseBodyPodRiskList()
                self.pod_risk_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPodRiskResponseBodyPodRiskList(DaraModel):
    def __init__(
        self,
        alarm_count: int = None,
        cluster_id: str = None,
        cluster_name: str = None,
        create_time: int = None,
        hc_count: int = None,
        instance_id: str = None,
        namespace: str = None,
        node_name: str = None,
        pod: str = None,
        pod_ip: str = None,
        vul_count: int = None,
    ):
        # The number of alerts that are generated for the pod.
        self.alarm_count = alarm_count
        # The ID of the container cluster.
        self.cluster_id = cluster_id
        # The name of the cluster.
        self.cluster_name = cluster_name
        # The timestamp that indicates the time when the pod was created. Unit: milliseconds.
        self.create_time = create_time
        # The number of baseline risk items that are detected in the pod.
        self.hc_count = hc_count
        # The instance ID of the node.
        self.instance_id = instance_id
        # The namespace of the Kubernetes cluster.
        self.namespace = namespace
        # The name of the node.
        self.node_name = node_name
        # The name of the pod.
        self.pod = pod
        # The IP address of the pod.
        self.pod_ip = pod_ip
        # The number of vulnerabilities that are detected in the pod.
        self.vul_count = vul_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_count is not None:
            result['AlarmCount'] = self.alarm_count

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.hc_count is not None:
            result['HcCount'] = self.hc_count

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.pod is not None:
            result['Pod'] = self.pod

        if self.pod_ip is not None:
            result['PodIp'] = self.pod_ip

        if self.vul_count is not None:
            result['VulCount'] = self.vul_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmCount') is not None:
            self.alarm_count = m.get('AlarmCount')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('HcCount') is not None:
            self.hc_count = m.get('HcCount')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('Pod') is not None:
            self.pod = m.get('Pod')

        if m.get('PodIp') is not None:
            self.pod_ip = m.get('PodIp')

        if m.get('VulCount') is not None:
            self.vul_count = m.get('VulCount')

        return self

class ListPodRiskResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

