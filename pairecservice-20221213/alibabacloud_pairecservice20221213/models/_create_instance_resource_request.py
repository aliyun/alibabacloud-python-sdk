# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateInstanceResourceRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        group: str = None,
        type: str = None,
        uri: str = None,
    ):
        # The resource category. Valid values:
        # 
        # - DataManagement
        # 
        # - Engine
        # 
        # - Monitor
        # 
        # This parameter is required.
        self.category = category
        # The resource group.
        # 
        # If the resource category is DataManagement, valid values are:
        # 
        # - storage
        # 
        # - modelpipeline
        # 
        # - datastorage
        # 
        # - modeltrain
        # 
        # If the resource category is Engine, valid values are:
        # 
        # - feature
        # 
        # - predict
        # 
        # - recall
        # 
        # - recengine
        # 
        # If the resource category is Monitor, valid values are:
        # 
        # - logs
        # 
        # - logsback
        # 
        # - coldstart
        # 
        # - deploy
        # 
        # This parameter is required.
        self.group = group
        # The resource type. Valid values:
        # 
        # - Hologres
        # 
        # - EAS
        # 
        # - BE
        # 
        # - Rec
        # 
        # - Platform
        # 
        # - SLS
        # 
        # - DataHub
        # 
        # - ApsaraMQ for Kafka
        # 
        # - Realtime Compute for Apache Flink
        # 
        # - ACR
        # 
        # - OSS
        # 
        # - DataWorks
        # 
        # - PAI
        # 
        # - MaxCompute
        # 
        # - Graph Compute
        # 
        # - ApsaraDB for Redis
        # 
        # This parameter is required.
        self.type = type
        # The resource URI.
        # 
        # This parameter is required.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.group is not None:
            result['Group'] = self.group

        if self.type is not None:
            result['Type'] = self.type

        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self

