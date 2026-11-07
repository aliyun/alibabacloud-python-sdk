# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateOrUpdateSwimmingLaneGroupRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        app_ids: str = None,
        canary_model: int = None,
        db_gray_enable: bool = None,
        entry_app: str = None,
        id: int = None,
        message_queue_filter_side: str = None,
        message_queue_gray_enable: bool = None,
        name: str = None,
        namespace: str = None,
        paths: List[str] = None,
        record_canary_detail: bool = None,
        region: str = None,
        route_ids: List[int] = None,
        status: int = None,
        swim_version: int = None,
    ):
        # The language of the response. Valid values:
        # - zh: Chinese.
        # - en: English.
        self.accept_language = accept_language
        # The IDs of the applications. Separate multiple IDs with commas (,).
        self.app_ids = app_ids
        # The end-to-end canary release mode. Valid values:
        # - 0: Route by request content.
        # - 1: Route by proportion.
        self.canary_model = canary_model
        # **[Deprecated]** Specifies whether to enable canary release for databases.
        self.db_gray_enable = db_gray_enable
        # The entry application. Format: Source system:ID. Examples:
        # - mse:${MSE application ID}
        # - mse-gw:${MSE cloud-native gateway ID}
        # - apig:${cloud-native API gateway ID}
        self.entry_app = entry_app
        # The ID of the swimlane group. A value of -1 indicates that a swimlane group is created. A value greater than 0 indicates that a specified swimlane group is updated.
        self.id = id
        # The side where message queue canary release filtering is performed.
        self.message_queue_filter_side = message_queue_filter_side
        # Specifies whether to enable canary release for message queues.
        self.message_queue_gray_enable = message_queue_gray_enable
        # The name of the swimlane group.
        # 
        # This parameter is required.
        self.name = name
        # The name of the MSE namespace.
        self.namespace = namespace
        # **[Deprecated]** The paths. This parameter is required when a Java gateway is used as the entry point.
        self.paths = paths
        # Specifies whether to record request details.
        self.record_canary_detail = record_canary_detail
        # The region.
        self.region = region
        # The IDs of the routes. If a cloud-native gateway is used as the entry point, you must call this operation to pass the IDs of the selected cloud-native gateway routes before creating a swimlane for the swimlane group.
        self.route_ids = route_ids
        # The status of the swimlane group. Valid values:
        # - 0: Inactive.
        # - 1: Active.
        self.status = status
        # The version of the end-to-end canary release. Valid values:
        # - 0: Not recommended. Routes must be specified.
        # - 2: Recommended. Routes do not need to be specified.
        self.swim_version = swim_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.app_ids is not None:
            result['AppIds'] = self.app_ids

        if self.canary_model is not None:
            result['CanaryModel'] = self.canary_model

        if self.db_gray_enable is not None:
            result['DbGrayEnable'] = self.db_gray_enable

        if self.entry_app is not None:
            result['EntryApp'] = self.entry_app

        if self.id is not None:
            result['Id'] = self.id

        if self.message_queue_filter_side is not None:
            result['MessageQueueFilterSide'] = self.message_queue_filter_side

        if self.message_queue_gray_enable is not None:
            result['MessageQueueGrayEnable'] = self.message_queue_gray_enable

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.paths is not None:
            result['Paths'] = self.paths

        if self.record_canary_detail is not None:
            result['RecordCanaryDetail'] = self.record_canary_detail

        if self.region is not None:
            result['Region'] = self.region

        if self.route_ids is not None:
            result['RouteIds'] = self.route_ids

        if self.status is not None:
            result['Status'] = self.status

        if self.swim_version is not None:
            result['SwimVersion'] = self.swim_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')

        if m.get('CanaryModel') is not None:
            self.canary_model = m.get('CanaryModel')

        if m.get('DbGrayEnable') is not None:
            self.db_gray_enable = m.get('DbGrayEnable')

        if m.get('EntryApp') is not None:
            self.entry_app = m.get('EntryApp')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MessageQueueFilterSide') is not None:
            self.message_queue_filter_side = m.get('MessageQueueFilterSide')

        if m.get('MessageQueueGrayEnable') is not None:
            self.message_queue_gray_enable = m.get('MessageQueueGrayEnable')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Paths') is not None:
            self.paths = m.get('Paths')

        if m.get('RecordCanaryDetail') is not None:
            self.record_canary_detail = m.get('RecordCanaryDetail')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RouteIds') is not None:
            self.route_ids = m.get('RouteIds')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SwimVersion') is not None:
            self.swim_version = m.get('SwimVersion')

        return self

