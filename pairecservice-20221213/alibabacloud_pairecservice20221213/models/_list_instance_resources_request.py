# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInstanceResourcesRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        group: str = None,
        type: str = None,
    ):
        # The category of the resource. Valid values:
        # 
        # - DataManagement
        # 
        # - Engine
        # 
        # - Monitor
        self.category = category
        # The group of the resource.
        # 
        # If `Category` is `DataManagement`, valid values are:
        # 
        # - storage
        # 
        # - modelpipeline
        # 
        # - datastorage
        # 
        # - modeltrain
        # 
        # If `Category` is `Engine`, valid values are:
        # 
        # - feature
        # 
        # - predict
        # 
        # - recall
        # 
        # - recengine
        # 
        # If `Category` is `Monitor`, valid values are:
        # 
        # - logs
        # 
        # - logsback
        # 
        # - coldstart
        # 
        # - deploy
        self.group = group
        # The type of the resource. If specified, only resources of this type are returned.
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
        # - Graph Compute Service
        # 
        # - ApsaraDB for Redis
        self.type = type

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

