# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetLatestSubmitDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        submit_detail_result: main_models.GetLatestSubmitDetailResponseBodySubmitDetailResult = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.submit_detail_result = submit_detail_result
        self.success = success

    def validate(self):
        if self.submit_detail_result:
            self.submit_detail_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.submit_detail_result is not None:
            result['SubmitDetailResult'] = self.submit_detail_result.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SubmitDetailResult') is not None:
            temp_model = main_models.GetLatestSubmitDetailResponseBodySubmitDetailResult()
            self.submit_detail_result = temp_model.from_map(m.get('SubmitDetailResult'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetLatestSubmitDetailResponseBodySubmitDetailResult(DaraModel):
    def __init__(
        self,
        id: int = None,
        publish_status: str = None,
        release_object: main_models.GetLatestSubmitDetailResponseBodySubmitDetailResultReleaseObject = None,
        submit_status: str = None,
        tag: str = None,
    ):
        self.id = id
        self.publish_status = publish_status
        self.release_object = release_object
        self.submit_status = submit_status
        self.tag = tag

    def validate(self):
        if self.release_object:
            self.release_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.publish_status is not None:
            result['PublishStatus'] = self.publish_status

        if self.release_object is not None:
            result['ReleaseObject'] = self.release_object.to_map()

        if self.submit_status is not None:
            result['SubmitStatus'] = self.submit_status

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('PublishStatus') is not None:
            self.publish_status = m.get('PublishStatus')

        if m.get('ReleaseObject') is not None:
            temp_model = main_models.GetLatestSubmitDetailResponseBodySubmitDetailResultReleaseObject()
            self.release_object = temp_model.from_map(m.get('ReleaseObject'))

        if m.get('SubmitStatus') is not None:
            self.submit_status = m.get('SubmitStatus')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

class GetLatestSubmitDetailResponseBodySubmitDetailResultReleaseObject(DaraModel):
    def __init__(
        self,
        change_type: str = None,
        node_id: str = None,
        object_version: str = None,
        project_id: int = None,
        submit_comment: str = None,
        submit_object: main_models.GetLatestSubmitDetailResponseBodySubmitDetailResultReleaseObjectSubmitObject = None,
    ):
        self.change_type = change_type
        self.node_id = node_id
        self.object_version = object_version
        self.project_id = project_id
        self.submit_comment = submit_comment
        self.submit_object = submit_object

    def validate(self):
        if self.submit_object:
            self.submit_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.change_type is not None:
            result['ChangeType'] = self.change_type

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.object_version is not None:
            result['ObjectVersion'] = self.object_version

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.submit_comment is not None:
            result['SubmitComment'] = self.submit_comment

        if self.submit_object is not None:
            result['SubmitObject'] = self.submit_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChangeType') is not None:
            self.change_type = m.get('ChangeType')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('ObjectVersion') is not None:
            self.object_version = m.get('ObjectVersion')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('SubmitComment') is not None:
            self.submit_comment = m.get('SubmitComment')

        if m.get('SubmitObject') is not None:
            temp_model = main_models.GetLatestSubmitDetailResponseBodySubmitDetailResultReleaseObjectSubmitObject()
            self.submit_object = temp_model.from_map(m.get('SubmitObject'))

        return self

class GetLatestSubmitDetailResponseBodySubmitDetailResultReleaseObjectSubmitObject(DaraModel):
    def __init__(
        self,
        object_id: str = None,
        object_name: str = None,
        object_type: str = None,
    ):
        self.object_id = object_id
        self.object_name = object_name
        self.object_type = object_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.object_name is not None:
            result['ObjectName'] = self.object_name

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        return self

