# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetServiceListenersRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        group_name: str = None,
        has_ip_count: str = None,
        instance_id: str = None,
        namespace_id: str = None,
        page_num: int = None,
        page_size: int = None,
        region_id: str = None,
        request_pars: str = None,
        service_name: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The ID of the MSE instance to which the service belongs.
        # 
        # >  You must specify InstanceId or ClusterId.
        self.cluster_id = cluster_id
        # The name of the cluster to which the service belongs.
        # 
        # > The cluster is a concept for Nacos services and is not equivalent to a Microservices Engine (MSE) instance.
        self.cluster_name = cluster_name
        # The group to which the service belongs.
        self.group_name = group_name
        # A reserved parameter.
        self.has_ip_count = has_ip_count
        # The ID of the instance to which the service belongs.
        # 
        # > You must specify InstanceId or ClusterId.
        self.instance_id = instance_id
        # The namespace to which the service belongs.
        self.namespace_id = namespace_id
        # The number of the page to return.
        self.page_num = page_num
        # The number of entries to return on each page.
        self.page_size = page_size
        # The ID of the region.
        self.region_id = region_id
        # The extended request parameters in the JSON format.
        self.request_pars = request_pars
        # The name of the service whose listeners you want to query.
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.has_ip_count is not None:
            result['HasIpCount'] = self.has_ip_count

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('HasIpCount') is not None:
            self.has_ip_count = m.get('HasIpCount')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        return self

