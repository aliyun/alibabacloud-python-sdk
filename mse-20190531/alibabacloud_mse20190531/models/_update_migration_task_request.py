# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateMigrationTaskRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        cluster_type: str = None,
        id: str = None,
        origin_instance_address: str = None,
        origin_instance_name: str = None,
        origin_instance_namespace: str = None,
        project_desc: str = None,
        request_pars: str = None,
        sync_type: str = None,
        target_cluster_name: str = None,
        target_cluster_url: str = None,
        target_instance_id: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The type of the instance. Valid values:
        # 
        # *   Nacos-Ans
        # *   ZooKeeper
        # *   Eureka
        self.cluster_type = cluster_type
        # The ID of the task.
        self.id = id
        # The address of the source instance node.
        self.origin_instance_address = origin_instance_address
        # The name of the source instance.
        self.origin_instance_name = origin_instance_name
        # The list of namespaces. This parameter is optional if you want to migrate applications from a Nacos instance.
        self.origin_instance_namespace = origin_instance_namespace
        # The description.
        self.project_desc = project_desc
        # The extended request parameters in the JSON format.
        self.request_pars = request_pars
        self.sync_type = sync_type
        # The name of the destination instance.
        self.target_cluster_name = target_cluster_name
        # The URL of the destination instance.
        self.target_cluster_url = target_cluster_url
        # The ID of the destination instance.
        self.target_instance_id = target_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.id is not None:
            result['Id'] = self.id

        if self.origin_instance_address is not None:
            result['OriginInstanceAddress'] = self.origin_instance_address

        if self.origin_instance_name is not None:
            result['OriginInstanceName'] = self.origin_instance_name

        if self.origin_instance_namespace is not None:
            result['OriginInstanceNamespace'] = self.origin_instance_namespace

        if self.project_desc is not None:
            result['ProjectDesc'] = self.project_desc

        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars

        if self.sync_type is not None:
            result['SyncType'] = self.sync_type

        if self.target_cluster_name is not None:
            result['TargetClusterName'] = self.target_cluster_name

        if self.target_cluster_url is not None:
            result['TargetClusterUrl'] = self.target_cluster_url

        if self.target_instance_id is not None:
            result['TargetInstanceId'] = self.target_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OriginInstanceAddress') is not None:
            self.origin_instance_address = m.get('OriginInstanceAddress')

        if m.get('OriginInstanceName') is not None:
            self.origin_instance_name = m.get('OriginInstanceName')

        if m.get('OriginInstanceNamespace') is not None:
            self.origin_instance_namespace = m.get('OriginInstanceNamespace')

        if m.get('ProjectDesc') is not None:
            self.project_desc = m.get('ProjectDesc')

        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')

        if m.get('SyncType') is not None:
            self.sync_type = m.get('SyncType')

        if m.get('TargetClusterName') is not None:
            self.target_cluster_name = m.get('TargetClusterName')

        if m.get('TargetClusterUrl') is not None:
            self.target_cluster_url = m.get('TargetClusterUrl')

        if m.get('TargetInstanceId') is not None:
            self.target_instance_id = m.get('TargetInstanceId')

        return self

