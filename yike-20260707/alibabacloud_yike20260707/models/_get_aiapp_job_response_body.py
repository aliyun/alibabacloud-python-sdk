# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yike20260707 import models as main_models
from darabonba.model import DaraModel

class GetAIAppJobResponseBody(DaraModel):
    def __init__(
        self,
        aiapp_job: main_models.GetAIAppJobResponseBodyAIAppJob = None,
        artifacts: List[main_models.GetAIAppJobResponseBodyArtifacts] = None,
        request_id: str = None,
    ):
        # The task information.
        self.aiapp_job = aiapp_job
        # The output assets.
        self.artifacts = artifacts
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.aiapp_job:
            self.aiapp_job.validate()
        if self.artifacts:
            for v1 in self.artifacts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aiapp_job is not None:
            result['AIAppJob'] = self.aiapp_job.to_map()

        result['Artifacts'] = []
        if self.artifacts is not None:
            for k1 in self.artifacts:
                result['Artifacts'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AIAppJob') is not None:
            temp_model = main_models.GetAIAppJobResponseBodyAIAppJob()
            self.aiapp_job = temp_model.from_map(m.get('AIAppJob'))

        self.artifacts = []
        if m.get('Artifacts') is not None:
            for k1 in m.get('Artifacts'):
                temp_model = main_models.GetAIAppJobResponseBodyArtifacts()
                self.artifacts.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAIAppJobResponseBodyArtifacts(DaraModel):
    def __init__(
        self,
        asset_id: str = None,
        name: str = None,
        status: str = None,
        type: str = None,
        url: str = None,
    ):
        # The asset ID, which is the media asset ID obtained after registration.
        self.asset_id = asset_id
        # The asset name.
        self.name = name
        # The asset status.
        self.status = status
        # The asset type. Valid values: image, audio, video, document, and text.
        self.type = type
        # The asset URL.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_id is not None:
            result['AssetId'] = self.asset_id

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetId') is not None:
            self.asset_id = m.get('AssetId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class GetAIAppJobResponseBodyAIAppJob(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        finish_time: str = None,
        job_id: str = None,
        node_results: str = None,
        outputs: str = None,
        status: str = None,
        user_data: str = None,
        version: str = None,
    ):
        # The time when the task was created.
        self.create_time = create_time
        # The time when the task was completed.
        self.finish_time = finish_time
        # The task ID.
        self.job_id = job_id
        # The node results of the workflow task. The results are in JSON format and vary based on the workflow configuration.
        self.node_results = node_results
        # The task outputs.
        self.outputs = outputs
        # The task status. Valid values:
        # - init: The task is created.
        # - running: The task is running.
        # - succeeded: The task succeeded.
        # - failed: The task failed.
        # - stopped: The task is stopped.
        self.status = status
        # The custom information.
        self.user_data = user_data
        # The application version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.node_results is not None:
            result['NodeResults'] = self.node_results

        if self.outputs is not None:
            result['Outputs'] = self.outputs

        if self.status is not None:
            result['Status'] = self.status

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('NodeResults') is not None:
            self.node_results = m.get('NodeResults')

        if m.get('Outputs') is not None:
            self.outputs = m.get('Outputs')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

