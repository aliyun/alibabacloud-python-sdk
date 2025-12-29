# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class ListUserKubeConfigStatesResponseBody(DaraModel):
    def __init__(
        self,
        page: main_models.ListUserKubeConfigStatesResponseBodyPage = None,
        states: List[main_models.ListUserKubeConfigStatesResponseBodyStates] = None,
    ):
        # The pagination information.
        self.page = page
        # The status of the kubeconfig files.
        self.states = states

    def validate(self):
        if self.page:
            self.page.validate()
        if self.states:
            for v1 in self.states:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page is not None:
            result['page'] = self.page.to_map()

        result['states'] = []
        if self.states is not None:
            for k1 in self.states:
                result['states'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page') is not None:
            temp_model = main_models.ListUserKubeConfigStatesResponseBodyPage()
            self.page = temp_model.from_map(m.get('page'))

        self.states = []
        if m.get('states') is not None:
            for k1 in m.get('states'):
                temp_model = main_models.ListUserKubeConfigStatesResponseBodyStates()
                self.states.append(temp_model.from_map(k1))

        return self

class ListUserKubeConfigStatesResponseBodyStates(DaraModel):
    def __init__(
        self,
        cert_expire_time: str = None,
        cert_state: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_state: str = None,
    ):
        # The expiration date of the certificate used in a kubeconfig file. Format: the UTC time in the RFC3339 format.
        self.cert_expire_time = cert_expire_time
        # The current status of the certificate used in a kubeconfig file. Valid values:
        # 
        # *   Expired: The certificate is expired.
        # *   Unexpired: The certificate is not expired.
        # *   Unissued: The certificate is not issued.
        # *   Unknown: The status of the certificate is unknown.
        # *   Removed: The certificate is removed. An issue record is found for the certificate.
        self.cert_state = cert_state
        # The cluster ID.
        self.cluster_id = cluster_id
        # The name of the cluster.
        # 
        # The name must be 1 to 63 characters in length, and can contain digits, underscores (_), and hyphens (-). The name must start with a letter or number.
        self.cluster_name = cluster_name
        # The status of the cluster. Valid values:
        # 
        # *   `initial`: The cluster is being created.
        # *   `failed`: The cluster failed to be created.
        # *   `running`: The cluster is running.
        # *   `updating`: The cluster is being upgraded.
        # *   `updating_failed`: The cluster failed to be updated.
        # *   `scaling`: The cluster is being scaled.
        # *   `stopped`: The cluster is stopped.
        # *   `deleting`: The cluster is being deleted.
        # *   `deleted`: The cluster is deleted.
        # *   `delete_failed`: The cluster failed to be deleted.
        self.cluster_state = cluster_state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_expire_time is not None:
            result['cert_expire_time'] = self.cert_expire_time

        if self.cert_state is not None:
            result['cert_state'] = self.cert_state

        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id

        if self.cluster_name is not None:
            result['cluster_name'] = self.cluster_name

        if self.cluster_state is not None:
            result['cluster_state'] = self.cluster_state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cert_expire_time') is not None:
            self.cert_expire_time = m.get('cert_expire_time')

        if m.get('cert_state') is not None:
            self.cert_state = m.get('cert_state')

        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')

        if m.get('cluster_name') is not None:
            self.cluster_name = m.get('cluster_name')

        if m.get('cluster_state') is not None:
            self.cluster_state = m.get('cluster_state')

        return self

class ListUserKubeConfigStatesResponseBodyPage(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['page_number'] = self.page_number

        if self.page_size is not None:
            result['page_size'] = self.page_size

        if self.total_count is not None:
            result['total_count'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')

        return self

