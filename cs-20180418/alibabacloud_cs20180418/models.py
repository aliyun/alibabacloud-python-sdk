# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class GetProjectEventsRequest(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class GetProjectEventsResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeKubernetesTemplateRequest(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeKubernetesTemplateResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeAgilityTunnelCertsRequest(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeAgilityTunnelCertsResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeClusterTokensRequest(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeClusterTokensResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DownloadClusterNodeCertsRequest(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DownloadClusterNodeCertsResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeServiceContainersRequest(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeServiceContainersResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class GatherLogsTokenRequest(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class GatherLogsTokenResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class GetClusterProjectsRequest(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class GetClusterProjectsResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeApiVersionRequest(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeApiVersionResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeTaskInfoRequest(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeTaskInfoResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeClusterNodesQuery(TeaModel):
    def __init__(self, page_size=None, page_number=None):
        self.page_size = page_size      # type: str
        self.page_number = page_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['pageSize'] = self.page_size
        result['pageNumber'] = self.page_number
        return result

    def from_map(self, map={}):
        self.page_size = map.get('pageSize')
        self.page_number = map.get('pageNumber')
        return self


class DescribeClusterNodesRequest(TeaModel):
    def __init__(self, headers=None, query=None):
        self.headers = headers          # type: Dict[str, str]
        self.query = query              # type: DescribeClusterNodesQuery

    def validate(self):
        if self.query:
            self.query.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.query is not None:
            result['query'] = self.query.to_map()
        else:
            result['query'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('query') is not None:
            temp_model = DescribeClusterNodesQuery()
            self.query = temp_model.from_map(map['query'])
        else:
            self.query = None
        return self


class DescribeClusterNodesResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeAgilityTunnelAgentInfoRequest(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeAgilityTunnelAgentInfoResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DeleteClusterNodeQuery(TeaModel):
    def __init__(self, force=None, release_instance=None):
        self.force = force              # type: str
        self.release_instance = release_instance  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['force'] = self.force
        result['releaseInstance'] = self.release_instance
        return result

    def from_map(self, map={}):
        self.force = map.get('force')
        self.release_instance = map.get('releaseInstance')
        return self


class DeleteClusterNodeRequest(TeaModel):
    def __init__(self, headers=None, query=None):
        self.headers = headers          # type: Dict[str, str]
        self.query = query              # type: DeleteClusterNodeQuery

    def validate(self):
        if self.query:
            self.query.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.query is not None:
            result['query'] = self.query.to_map()
        else:
            result['query'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('query') is not None:
            temp_model = DeleteClusterNodeQuery()
            self.query = temp_model.from_map(map['query'])
        else:
            self.query = None
        return self


class DeleteClusterNodeResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeClusterNodeInfoWithInstanceRequest(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeClusterNodeInfoWithInstanceResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeUserContainersQuery(TeaModel):
    def __init__(self, service_id=None):
        self.service_id = service_id    # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ServiceId'] = self.service_id
        return result

    def from_map(self, map={}):
        self.service_id = map.get('ServiceId')
        return self


class DescribeUserContainersRequest(TeaModel):
    def __init__(self, headers=None, query=None):
        self.headers = headers          # type: Dict[str, str]
        self.query = query              # type: DescribeUserContainersQuery

    def validate(self):
        if self.query:
            self.query.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.query is not None:
            result['query'] = self.query.to_map()
        else:
            result['query'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('query') is not None:
            temp_model = DescribeUserContainersQuery()
            self.query = temp_model.from_map(map['query'])
        else:
            self.query = None
        return self


class DescribeUserContainersResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class CreateClusterTokenRequest(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class CreateClusterTokenResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeClusterHostsRequest(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeClusterHostsResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeKubernetesTemplatesQuery(TeaModel):
    def __init__(self, kubernetes_version=None, region=None):
        self.kubernetes_version = kubernetes_version  # type: str
        self.region = region            # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['KubernetesVersion'] = self.kubernetes_version
        result['Region'] = self.region
        return result

    def from_map(self, map={}):
        self.kubernetes_version = map.get('KubernetesVersion')
        self.region = map.get('Region')
        return self


class DescribeKubernetesTemplatesRequest(TeaModel):
    def __init__(self, headers=None, query=None):
        self.headers = headers          # type: Dict[str, str]
        self.query = query              # type: DescribeKubernetesTemplatesQuery

    def validate(self):
        if self.query:
            self.query.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.query is not None:
            result['query'] = self.query.to_map()
        else:
            result['query'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('query') is not None:
            temp_model = DescribeKubernetesTemplatesQuery()
            self.query = temp_model.from_map(map['query'])
        else:
            self.query = None
        return self


class DescribeKubernetesTemplatesResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeTemplatesRequest(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeTemplatesResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeClusterScaledNodeRequest(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeClusterScaledNodeResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class CallbackClusterTokenRequest(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class CallbackClusterTokenResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeImagesQuery(TeaModel):
    def __init__(self, region_id=None, docker_version=None, image_name=None):
        self.region_id = region_id      # type: str
        self.docker_version = docker_version  # type: str
        self.image_name = image_name    # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['RegionID'] = self.region_id
        result['DockerVersion'] = self.docker_version
        result['ImageName'] = self.image_name
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionID')
        self.docker_version = map.get('DockerVersion')
        self.image_name = map.get('ImageName')
        return self


class DescribeImagesRequest(TeaModel):
    def __init__(self, headers=None, query=None):
        self.headers = headers          # type: Dict[str, str]
        self.query = query              # type: DescribeImagesQuery

    def validate(self):
        if self.query:
            self.query.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.query is not None:
            result['query'] = self.query.to_map()
        else:
            result['query'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('query') is not None:
            temp_model = DescribeImagesQuery()
            self.query = temp_model.from_map(map['query'])
        else:
            self.query = None
        return self


class DescribeImagesResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeClusterLogsRequest(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeClusterLogsResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeClusterServicesRequest(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeClusterServicesResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class GetTriggerHookRequest(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class GetTriggerHookResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeTemplateAttributeRequest(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeTemplateAttributeResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeClusterCertsRequest(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeClusterCertsResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeClusterNodeInfoRequest(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeClusterNodeInfoResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DeleteClusterRequest(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DeleteClusterResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class CreateClusterRequest(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class CreateClusterResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeClusterDetailRequest(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeClusterDetailResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeClustersQuery(TeaModel):
    def __init__(self, name=None, cluster_type=None):
        self.name = name                # type: str
        self.cluster_type = cluster_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['clusterType'] = self.cluster_type
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.cluster_type = map.get('clusterType')
        return self


class DescribeClustersRequest(TeaModel):
    def __init__(self, headers=None, query=None):
        self.headers = headers          # type: Dict[str, str]
        self.query = query              # type: DescribeClustersQuery

    def validate(self):
        if self.query:
            self.query.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.query is not None:
            result['query'] = self.query.to_map()
        else:
            result['query'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('query') is not None:
            temp_model = DescribeClustersQuery()
            self.query = temp_model.from_map(map['query'])
        else:
            self.query = None
        return self


class DescribeClustersResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self
