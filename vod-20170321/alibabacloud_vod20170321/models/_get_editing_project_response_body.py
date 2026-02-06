# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class GetEditingProjectResponseBody(DaraModel):
    def __init__(
        self,
        project: main_models.GetEditingProjectResponseBodyProject = None,
        request_id: str = None,
    ):
        # The information about the online editing project.
        self.project = project
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.project:
            self.project.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project is not None:
            result['Project'] = self.project.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Project') is not None:
            temp_model = main_models.GetEditingProjectResponseBodyProject()
            self.project = temp_model.from_map(m.get('Project'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetEditingProjectResponseBodyProject(DaraModel):
    def __init__(
        self,
        cover_url: str = None,
        creation_time: str = None,
        description: str = None,
        modified_time: str = None,
        project_id: str = None,
        region_id: str = None,
        status: str = None,
        storage_location: str = None,
        timeline: str = None,
        title: str = None,
    ):
        # The thumbnail URL of the online editing project.
        self.cover_url = cover_url
        # The time when the online editing project was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The description of the online editing project.
        self.description = description
        # The last time when the online editing project was modified. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.modified_time = modified_time
        # The ID of the online editing project.
        self.project_id = project_id
        # The region where the online editing project was created.
        self.region_id = region_id
        # The status of the online editing project. Separate multiple states with commas (,). By default, all online editing projects were queried. Valid values:
        # 
        # *   **Normal**: indicates that the online editing project is in draft.
        # *   **Producing**: indicates that the video is being produced.
        # *   **Produced**: indicates that the video was produced.
        # *   **ProduceFailed**: indicates that the video failed to be produced.
        self.status = status
        # The path of the Object Storage Service (OSS) bucket where the online editing project is stored.
        # 
        # > To view the path of the OSS bucket, log on to the [ApsaraVideo VOD console](https://vod.console.aliyun.com/?spm=a2c4g.11186623.2.15.6948257eaZ4m54#/vod/settings/censored), and choose **Configuration Management** > **Media Management** > **Storage**. On the Storage page, you can view the path of the OSS bucket.
        self.storage_location = storage_location
        # The timeline of the online editing project.
        self.timeline = timeline
        # The title of the online editing project.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cover_url is not None:
            result['CoverURL'] = self.cover_url

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_location is not None:
            result['StorageLocation'] = self.storage_location

        if self.timeline is not None:
            result['Timeline'] = self.timeline

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoverURL') is not None:
            self.cover_url = m.get('CoverURL')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageLocation') is not None:
            self.storage_location = m.get('StorageLocation')

        if m.get('Timeline') is not None:
            self.timeline = m.get('Timeline')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

