# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateJenkinsImageScanTaskRequest(DaraModel):
    def __init__(
        self,
        digest: str = None,
        image_create: int = None,
        image_id: str = None,
        image_size: int = None,
        image_update: int = None,
        jenkins_env: str = None,
        namespace: str = None,
        repo_name: str = None,
        source_ip: str = None,
        tag: str = None,
        token: str = None,
        uuid: str = None,
    ):
        # The image summary.
        self.digest = digest
        # The image creation time.
        self.image_create = image_create
        # The image ID.
        self.image_id = image_id
        # The image size. Unit: bytes.
        self.image_size = image_size
        # The image update time. The value is a UNIX timestamp. Unit: milliseconds.
        self.image_update = image_update
        # The Jenkins environment context. Leave this parameter empty or set it to the fixed value: **release**.
        self.jenkins_env = jenkins_env
        # The namespace.
        self.namespace = namespace
        # The repository name.
        self.repo_name = repo_name
        # The access source IP address.
        self.source_ip = source_ip
        # The image label.
        self.tag = tag
        # The access token for the Jenkins image repository. Obtain the token from the homepage of the Chinese documentation center > Security Center > User Guide > Container Protection > CI/CD Access Settings. You can also invoke CreateJenkinsImageRegistry to create a CI/CD image repository and obtain the token from the response parameter Data.Token. For an existing repository, invoke PageImageRegistry to query the token.
        self.token = token
        # The UUID of the image asset.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.digest is not None:
            result['Digest'] = self.digest

        if self.image_create is not None:
            result['ImageCreate'] = self.image_create

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_size is not None:
            result['ImageSize'] = self.image_size

        if self.image_update is not None:
            result['ImageUpdate'] = self.image_update

        if self.jenkins_env is not None:
            result['JenkinsEnv'] = self.jenkins_env

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.repo_name is not None:
            result['RepoName'] = self.repo_name

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.token is not None:
            result['Token'] = self.token

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')

        if m.get('ImageCreate') is not None:
            self.image_create = m.get('ImageCreate')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageSize') is not None:
            self.image_size = m.get('ImageSize')

        if m.get('ImageUpdate') is not None:
            self.image_update = m.get('ImageUpdate')

        if m.get('JenkinsEnv') is not None:
            self.jenkins_env = m.get('JenkinsEnv')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

