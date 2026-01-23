# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cr20181201 import models as main_models
from darabonba.model import DaraModel

class ListRepoBuildRuleResponseBody(DaraModel):
    def __init__(
        self,
        build_rules: List[main_models.ListRepoBuildRuleResponseBodyBuildRules] = None,
        code: str = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The list of image building rules.
        self.build_rules = build_rules
        # The return value.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The page number of the returned page.
        self.page_no = page_no
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.build_rules:
            for v1 in self.build_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BuildRules'] = []
        if self.build_rules is not None:
            for k1 in self.build_rules:
                result['BuildRules'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['Code'] = self.code

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.build_rules = []
        if m.get('BuildRules') is not None:
            for k1 in m.get('BuildRules'):
                temp_model = main_models.ListRepoBuildRuleResponseBodyBuildRules()
                self.build_rules.append(temp_model.from_map(k1))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRepoBuildRuleResponseBodyBuildRules(DaraModel):
    def __init__(
        self,
        build_args: List[str] = None,
        build_rule_id: str = None,
        dest_artifact_type: str = None,
        dockerfile_location: str = None,
        dockerfile_name: str = None,
        image_tag: str = None,
        platforms: List[str] = None,
        push_name: str = None,
        push_type: str = None,
    ):
        self.build_args = build_args
        # The ID of the image building rule.
        self.build_rule_id = build_rule_id
        self.dest_artifact_type = dest_artifact_type
        # The directory of the Dockerfile.
        self.dockerfile_location = dockerfile_location
        # The name of the Dockerfile.
        self.dockerfile_name = dockerfile_name
        # The tag of the image.
        self.image_tag = image_tag
        self.platforms = platforms
        # The name of the push that triggers the building rule.
        self.push_name = push_name
        # The type of the push that triggers the image building rule. Valid values:
        # 
        # *   GIT_BRANCH: branch push
        # *   GIT_TAG: tag push
        self.push_type = push_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.build_args is not None:
            result['BuildArgs'] = self.build_args

        if self.build_rule_id is not None:
            result['BuildRuleId'] = self.build_rule_id

        if self.dest_artifact_type is not None:
            result['DestArtifactType'] = self.dest_artifact_type

        if self.dockerfile_location is not None:
            result['DockerfileLocation'] = self.dockerfile_location

        if self.dockerfile_name is not None:
            result['DockerfileName'] = self.dockerfile_name

        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag

        if self.platforms is not None:
            result['Platforms'] = self.platforms

        if self.push_name is not None:
            result['PushName'] = self.push_name

        if self.push_type is not None:
            result['PushType'] = self.push_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildArgs') is not None:
            self.build_args = m.get('BuildArgs')

        if m.get('BuildRuleId') is not None:
            self.build_rule_id = m.get('BuildRuleId')

        if m.get('DestArtifactType') is not None:
            self.dest_artifact_type = m.get('DestArtifactType')

        if m.get('DockerfileLocation') is not None:
            self.dockerfile_location = m.get('DockerfileLocation')

        if m.get('DockerfileName') is not None:
            self.dockerfile_name = m.get('DockerfileName')

        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')

        if m.get('Platforms') is not None:
            self.platforms = m.get('Platforms')

        if m.get('PushName') is not None:
            self.push_name = m.get('PushName')

        if m.get('PushType') is not None:
            self.push_type = m.get('PushType')

        return self

