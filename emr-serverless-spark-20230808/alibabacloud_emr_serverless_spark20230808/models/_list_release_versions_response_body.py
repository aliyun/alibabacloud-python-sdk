# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class ListReleaseVersionsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        release_versions: List[main_models.ListReleaseVersionsResponseBodyReleaseVersions] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of entries returned.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The versions.
        self.release_versions = release_versions
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.release_versions:
            for v1 in self.release_versions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        result['releaseVersions'] = []
        if self.release_versions is not None:
            for k1 in self.release_versions:
                result['releaseVersions'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        self.release_versions = []
        if m.get('releaseVersions') is not None:
            for k1 in m.get('releaseVersions'):
                temp_model = main_models.ListReleaseVersionsResponseBodyReleaseVersions()
                self.release_versions.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListReleaseVersionsResponseBodyReleaseVersions(DaraModel):
    def __init__(
        self,
        community_version: str = None,
        cpu_architectures: List[str] = None,
        display_release_version: str = None,
        fusion: bool = None,
        gmt_create: int = None,
        iaas_type: str = None,
        release_version: str = None,
        scala_version: str = None,
        state: str = None,
        type: str = None,
    ):
        # The version number of open source Spark.
        self.community_version = community_version
        # The CPU architectures.
        self.cpu_architectures = cpu_architectures
        # The version number.
        self.display_release_version = display_release_version
        # Indicates whether the Fusion engine is used for acceleration.
        self.fusion = fusion
        # The creation time.
        self.gmt_create = gmt_create
        # The type of the Infrastructure as a Service (IaaS) layer.
        self.iaas_type = iaas_type
        # The version number.
        self.release_version = release_version
        # The version of Scala.
        self.scala_version = scala_version
        # The status of the version.
        self.state = state
        # The type of the version.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.community_version is not None:
            result['communityVersion'] = self.community_version

        if self.cpu_architectures is not None:
            result['cpuArchitectures'] = self.cpu_architectures

        if self.display_release_version is not None:
            result['displayReleaseVersion'] = self.display_release_version

        if self.fusion is not None:
            result['fusion'] = self.fusion

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.iaas_type is not None:
            result['iaasType'] = self.iaas_type

        if self.release_version is not None:
            result['releaseVersion'] = self.release_version

        if self.scala_version is not None:
            result['scalaVersion'] = self.scala_version

        if self.state is not None:
            result['state'] = self.state

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('communityVersion') is not None:
            self.community_version = m.get('communityVersion')

        if m.get('cpuArchitectures') is not None:
            self.cpu_architectures = m.get('cpuArchitectures')

        if m.get('displayReleaseVersion') is not None:
            self.display_release_version = m.get('displayReleaseVersion')

        if m.get('fusion') is not None:
            self.fusion = m.get('fusion')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('iaasType') is not None:
            self.iaas_type = m.get('iaasType')

        if m.get('releaseVersion') is not None:
            self.release_version = m.get('releaseVersion')

        if m.get('scalaVersion') is not None:
            self.scala_version = m.get('scalaVersion')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

