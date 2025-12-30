# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpc20240730 import models as main_models
from darabonba.model import DaraModel

class GetCommonLogDetailResponseBody(DaraModel):
    def __init__(
        self,
        action: str = None,
        cluster_id: str = None,
        log_detail: List[main_models.GetCommonLogDetailResponseBodyLogDetail] = None,
        log_type: str = None,
        operator_uid: str = None,
        request_id: str = None,
        uid: str = None,
    ):
        # The action name.
        self.action = action
        # The cluster ID.
        self.cluster_id = cluster_id
        # The information about the logs.
        self.log_detail = log_detail
        # The log type.
        self.log_type = log_type
        # The account ID of the operator.
        self.operator_uid = operator_uid
        # The request ID.
        self.request_id = request_id
        # The ID of the Alibaba Cloud account.
        self.uid = uid

    def validate(self):
        if self.log_detail:
            for v1 in self.log_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        result['LogDetail'] = []
        if self.log_detail is not None:
            for k1 in self.log_detail:
                result['LogDetail'].append(k1.to_map() if k1 else None)

        if self.log_type is not None:
            result['LogType'] = self.log_type

        if self.operator_uid is not None:
            result['OperatorUid'] = self.operator_uid

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        self.log_detail = []
        if m.get('LogDetail') is not None:
            for k1 in m.get('LogDetail'):
                temp_model = main_models.GetCommonLogDetailResponseBodyLogDetail()
                self.log_detail.append(temp_model.from_map(k1))

        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')

        if m.get('OperatorUid') is not None:
            self.operator_uid = m.get('OperatorUid')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

class GetCommonLogDetailResponseBodyLogDetail(DaraModel):
    def __init__(
        self,
        stage_name: str = None,
        stages: List[main_models.GetCommonLogDetailResponseBodyLogDetailStages] = None,
    ):
        # The stage name of the log.
        self.stage_name = stage_name
        # The information about the log stages.
        self.stages = stages

    def validate(self):
        if self.stages:
            for v1 in self.stages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.stage_name is not None:
            result['StageName'] = self.stage_name

        result['Stages'] = []
        if self.stages is not None:
            for k1 in self.stages:
                result['Stages'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')

        self.stages = []
        if m.get('Stages') is not None:
            for k1 in m.get('Stages'):
                temp_model = main_models.GetCommonLogDetailResponseBodyLogDetailStages()
                self.stages.append(temp_model.from_map(k1))

        return self

class GetCommonLogDetailResponseBodyLogDetailStages(DaraModel):
    def __init__(
        self,
        log_level: str = None,
        message: str = None,
        method: str = None,
        request_id: str = None,
        status: str = None,
        target: str = None,
        time: str = None,
    ):
        # The log level.
        # 
        # Valid values:
        # 
        # *   ERROR
        # *   INFO
        # *   WARN
        self.log_level = log_level
        # The output message of the log.
        self.message = message
        # The method involved in the log.
        self.method = method
        # The request ID associated with the log.
        self.request_id = request_id
        # The action state involved in the log. Valid values:
        # 
        # *   InProgress: The action is being performed.
        # *   Finished: The action is completed.
        # *   Failed: The action failed.
        self.status = status
        # The resource involved in the log.
        self.target = target
        # The time when the log was generated.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_level is not None:
            result['LogLevel'] = self.log_level

        if self.message is not None:
            result['Message'] = self.message

        if self.method is not None:
            result['Method'] = self.method

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.target is not None:
            result['Target'] = self.target

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogLevel') is not None:
            self.log_level = m.get('LogLevel')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

