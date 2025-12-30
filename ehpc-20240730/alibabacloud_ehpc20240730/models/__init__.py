# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from ._addon_node_template import AddonNodeTemplate
from ._node_template import NodeTemplate
from ._queue_template import QueueTemplate
from ._shared_storage_template import SharedStorageTemplate
from ._attach_nodes_request import AttachNodesRequest
from ._attach_nodes_shrink_request import AttachNodesShrinkRequest
from ._attach_nodes_response_body import AttachNodesResponseBody
from ._attach_nodes_response import AttachNodesResponse
from ._attach_shared_storages_request import AttachSharedStoragesRequest
from ._attach_shared_storages_shrink_request import AttachSharedStoragesShrinkRequest
from ._attach_shared_storages_response_body import AttachSharedStoragesResponseBody
from ._attach_shared_storages_response import AttachSharedStoragesResponse
from ._create_cluster_request import CreateClusterRequest
from ._create_cluster_shrink_request import CreateClusterShrinkRequest
from ._create_cluster_response_body import CreateClusterResponseBody
from ._create_cluster_response import CreateClusterResponse
from ._create_job_request import CreateJobRequest
from ._create_job_shrink_request import CreateJobShrinkRequest
from ._create_job_response_body import CreateJobResponseBody
from ._create_job_response import CreateJobResponse
from ._create_nodes_request import CreateNodesRequest
from ._create_nodes_shrink_request import CreateNodesShrinkRequest
from ._create_nodes_response_body import CreateNodesResponseBody
from ._create_nodes_response import CreateNodesResponse
from ._create_queue_request import CreateQueueRequest
from ._create_queue_shrink_request import CreateQueueShrinkRequest
from ._create_queue_response_body import CreateQueueResponseBody
from ._create_queue_response import CreateQueueResponse
from ._create_users_request import CreateUsersRequest
from ._create_users_shrink_request import CreateUsersShrinkRequest
from ._create_users_response_body import CreateUsersResponseBody
from ._create_users_response import CreateUsersResponse
from ._delete_cluster_request import DeleteClusterRequest
from ._delete_cluster_response_body import DeleteClusterResponseBody
from ._delete_cluster_response import DeleteClusterResponse
from ._delete_nodes_request import DeleteNodesRequest
from ._delete_nodes_shrink_request import DeleteNodesShrinkRequest
from ._delete_nodes_response_body import DeleteNodesResponseBody
from ._delete_nodes_response import DeleteNodesResponse
from ._delete_queues_request import DeleteQueuesRequest
from ._delete_queues_shrink_request import DeleteQueuesShrinkRequest
from ._delete_queues_response_body import DeleteQueuesResponseBody
from ._delete_queues_response import DeleteQueuesResponse
from ._delete_users_request import DeleteUsersRequest
from ._delete_users_shrink_request import DeleteUsersShrinkRequest
from ._delete_users_response_body import DeleteUsersResponseBody
from ._delete_users_response import DeleteUsersResponse
from ._describe_addon_template_request import DescribeAddonTemplateRequest
from ._describe_addon_template_response_body import DescribeAddonTemplateResponseBody
from ._describe_addon_template_response import DescribeAddonTemplateResponse
from ._detach_shared_storages_request import DetachSharedStoragesRequest
from ._detach_shared_storages_shrink_request import DetachSharedStoragesShrinkRequest
from ._detach_shared_storages_response_body import DetachSharedStoragesResponseBody
from ._detach_shared_storages_response import DetachSharedStoragesResponse
from ._get_addon_request import GetAddonRequest
from ._get_addon_response_body import GetAddonResponseBody
from ._get_addon_response import GetAddonResponse
from ._get_cluster_request import GetClusterRequest
from ._get_cluster_response_body import GetClusterResponseBody
from ._get_cluster_response import GetClusterResponse
from ._get_common_log_detail_request import GetCommonLogDetailRequest
from ._get_common_log_detail_response_body import GetCommonLogDetailResponseBody
from ._get_common_log_detail_response import GetCommonLogDetailResponse
from ._get_job_request import GetJobRequest
from ._get_job_response_body import GetJobResponseBody
from ._get_job_response import GetJobResponse
from ._get_job_log_request import GetJobLogRequest
from ._get_job_log_response_body import GetJobLogResponseBody
from ._get_job_log_response import GetJobLogResponse
from ._get_queue_request import GetQueueRequest
from ._get_queue_response_body import GetQueueResponseBody
from ._get_queue_response import GetQueueResponse
from ._install_addon_request import InstallAddonRequest
from ._install_addon_response_body import InstallAddonResponseBody
from ._install_addon_response import InstallAddonResponse
from ._install_softwares_request import InstallSoftwaresRequest
from ._install_softwares_shrink_request import InstallSoftwaresShrinkRequest
from ._install_softwares_response_body import InstallSoftwaresResponseBody
from ._install_softwares_response import InstallSoftwaresResponse
from ._list_addon_templates_request import ListAddonTemplatesRequest
from ._list_addon_templates_response_body import ListAddonTemplatesResponseBody
from ._list_addon_templates_response import ListAddonTemplatesResponse
from ._list_addons_request import ListAddonsRequest
from ._list_addons_shrink_request import ListAddonsShrinkRequest
from ._list_addons_response_body import ListAddonsResponseBody
from ._list_addons_response import ListAddonsResponse
from ._list_available_file_systems_request import ListAvailableFileSystemsRequest
from ._list_available_file_systems_response_body import ListAvailableFileSystemsResponseBody
from ._list_available_file_systems_response import ListAvailableFileSystemsResponse
from ._list_available_images_request import ListAvailableImagesRequest
from ._list_available_images_shrink_request import ListAvailableImagesShrinkRequest
from ._list_available_images_response_body import ListAvailableImagesResponseBody
from ._list_available_images_response import ListAvailableImagesResponse
from ._list_clusters_request import ListClustersRequest
from ._list_clusters_shrink_request import ListClustersShrinkRequest
from ._list_clusters_response_body import ListClustersResponseBody
from ._list_clusters_response import ListClustersResponse
from ._list_common_logs_request import ListCommonLogsRequest
from ._list_common_logs_shrink_request import ListCommonLogsShrinkRequest
from ._list_common_logs_response_body import ListCommonLogsResponseBody
from ._list_common_logs_response import ListCommonLogsResponse
from ._list_installed_softwares_request import ListInstalledSoftwaresRequest
from ._list_installed_softwares_response_body import ListInstalledSoftwaresResponseBody
from ._list_installed_softwares_response import ListInstalledSoftwaresResponse
from ._list_jobs_request import ListJobsRequest
from ._list_jobs_shrink_request import ListJobsShrinkRequest
from ._list_jobs_response_body import ListJobsResponseBody
from ._list_jobs_response import ListJobsResponse
from ._list_nodes_request import ListNodesRequest
from ._list_nodes_shrink_request import ListNodesShrinkRequest
from ._list_nodes_response_body import ListNodesResponseBody
from ._list_nodes_response import ListNodesResponse
from ._list_queues_request import ListQueuesRequest
from ._list_queues_shrink_request import ListQueuesShrinkRequest
from ._list_queues_response_body import ListQueuesResponseBody
from ._list_queues_response import ListQueuesResponse
from ._list_regions_request import ListRegionsRequest
from ._list_regions_response_body import ListRegionsResponseBody
from ._list_regions_response import ListRegionsResponse
from ._list_shared_storages_request import ListSharedStoragesRequest
from ._list_shared_storages_response_body import ListSharedStoragesResponseBody
from ._list_shared_storages_response import ListSharedStoragesResponse
from ._list_softwares_request import ListSoftwaresRequest
from ._list_softwares_response_body import ListSoftwaresResponseBody
from ._list_softwares_response import ListSoftwaresResponse
from ._list_users_request import ListUsersRequest
from ._list_users_response_body import ListUsersResponseBody
from ._list_users_response import ListUsersResponse
from ._stop_jobs_request import StopJobsRequest
from ._stop_jobs_shrink_request import StopJobsShrinkRequest
from ._stop_jobs_response_body import StopJobsResponseBody
from ._stop_jobs_response import StopJobsResponse
from ._un_install_addon_request import UnInstallAddonRequest
from ._un_install_addon_response_body import UnInstallAddonResponseBody
from ._un_install_addon_response import UnInstallAddonResponse
from ._uninstall_softwares_request import UninstallSoftwaresRequest
from ._uninstall_softwares_shrink_request import UninstallSoftwaresShrinkRequest
from ._uninstall_softwares_response_body import UninstallSoftwaresResponseBody
from ._uninstall_softwares_response import UninstallSoftwaresResponse
from ._update_cluster_request import UpdateClusterRequest
from ._update_cluster_shrink_request import UpdateClusterShrinkRequest
from ._update_cluster_response_body import UpdateClusterResponseBody
from ._update_cluster_response import UpdateClusterResponse
from ._update_nodes_request import UpdateNodesRequest
from ._update_nodes_shrink_request import UpdateNodesShrinkRequest
from ._update_nodes_response_body import UpdateNodesResponseBody
from ._update_nodes_response import UpdateNodesResponse
from ._update_queue_request import UpdateQueueRequest
from ._update_queue_shrink_request import UpdateQueueShrinkRequest
from ._update_queue_response_body import UpdateQueueResponseBody
from ._update_queue_response import UpdateQueueResponse
from ._update_user_request import UpdateUserRequest
from ._update_user_response_body import UpdateUserResponseBody
from ._update_user_response import UpdateUserResponse
from ._addon_node_template import AddonNodeTemplateDataDisks
from ._addon_node_template import AddonNodeTemplateSystemDisk
from ._node_template import NodeTemplateDataDisks
from ._node_template import NodeTemplateSystemDisk
from ._attach_nodes_request import AttachNodesRequestComputeNode
from ._attach_shared_storages_request import AttachSharedStoragesRequestSharedStorages
from ._create_cluster_request import CreateClusterRequestAdditionalPackages
from ._create_cluster_request import CreateClusterRequestAddons
from ._create_cluster_request import CreateClusterRequestClusterCredentials
from ._create_cluster_request import CreateClusterRequestClusterCustomConfiguration
from ._create_cluster_request import CreateClusterRequestManagerDNS
from ._create_cluster_request import CreateClusterRequestManagerDirectoryService
from ._create_cluster_request import CreateClusterRequestManagerScheduler
from ._create_cluster_request import CreateClusterRequestManager
from ._create_cluster_request import CreateClusterRequestTags
from ._create_job_request import CreateJobRequestJobSpecResources
from ._create_job_request import CreateJobRequestJobSpec
from ._create_users_request import CreateUsersRequestUser
from ._delete_users_request import DeleteUsersRequestUser
from ._describe_addon_template_response_body import DescribeAddonTemplateResponseBodyAddonResourcesSpecEipResource
from ._describe_addon_template_response_body import DescribeAddonTemplateResponseBodyAddonResourcesSpec
from ._describe_addon_template_response_body import DescribeAddonTemplateResponseBodyAddonServicesSpecInputParams
from ._describe_addon_template_response_body import DescribeAddonTemplateResponseBodyAddonServicesSpecNetworkACL
from ._describe_addon_template_response_body import DescribeAddonTemplateResponseBodyAddonServicesSpec
from ._describe_addon_template_response_body import DescribeAddonTemplateResponseBodyAddon
from ._detach_shared_storages_request import DetachSharedStoragesRequestSharedStorages
from ._get_addon_response_body import GetAddonResponseBodyAddonResourcesSpecEipResource
from ._get_addon_response_body import GetAddonResponseBodyAddonResourcesSpec
from ._get_addon_response_body import GetAddonResponseBodyAddonServicesSpecInputParams
from ._get_addon_response_body import GetAddonResponseBodyAddonServicesSpecNetworkACL
from ._get_addon_response_body import GetAddonResponseBodyAddonServicesSpec
from ._get_addon_response_body import GetAddonResponseBodyAddon
from ._get_cluster_response_body import GetClusterResponseBodyClusterCustomConfiguration
from ._get_cluster_response_body import GetClusterResponseBodyManagerDNS
from ._get_cluster_response_body import GetClusterResponseBodyManagerDirectoryService
from ._get_cluster_response_body import GetClusterResponseBodyManagerManagerNodeSystemDisk
from ._get_cluster_response_body import GetClusterResponseBodyManagerManagerNode
from ._get_cluster_response_body import GetClusterResponseBodyManagerScheduler
from ._get_cluster_response_body import GetClusterResponseBodyManager
from ._get_cluster_response_body import GetClusterResponseBodyMonitorSpec
from ._get_cluster_response_body import GetClusterResponseBodySchedulerSpec
from ._get_common_log_detail_response_body import GetCommonLogDetailResponseBodyLogDetailStages
from ._get_common_log_detail_response_body import GetCommonLogDetailResponseBodyLogDetail
from ._get_job_response_body import GetJobResponseBodyJobInfoResources
from ._get_job_response_body import GetJobResponseBodyJobInfoResourcesUsed
from ._get_job_response_body import GetJobResponseBodyJobInfoVariables
from ._get_job_response_body import GetJobResponseBodyJobInfo
from ._get_queue_response_body import GetQueueResponseBodyQueue
from ._install_softwares_request import InstallSoftwaresRequestAdditionalPackages
from ._list_addon_templates_response_body import ListAddonTemplatesResponseBodyAddons
from ._list_addons_response_body import ListAddonsResponseBodyAddons
from ._list_available_file_systems_response_body import ListAvailableFileSystemsResponseBodyFileSystemListMountTargetList
from ._list_available_file_systems_response_body import ListAvailableFileSystemsResponseBodyFileSystemList
from ._list_available_images_request import ListAvailableImagesRequestDirectoryService
from ._list_available_images_request import ListAvailableImagesRequestScheduler
from ._list_available_images_response_body import ListAvailableImagesResponseBodyImages
from ._list_clusters_response_body import ListClustersResponseBodyClustersAdditionalPackages
from ._list_clusters_response_body import ListClustersResponseBodyClustersAddonsResourcesSpec
from ._list_clusters_response_body import ListClustersResponseBodyClustersAddonsServicesSpec
from ._list_clusters_response_body import ListClustersResponseBodyClustersAddons
from ._list_clusters_response_body import ListClustersResponseBodyClustersClusterCustomConfiguration
from ._list_clusters_response_body import ListClustersResponseBodyClustersManagerDNS
from ._list_clusters_response_body import ListClustersResponseBodyClustersManagerDirectoryService
from ._list_clusters_response_body import ListClustersResponseBodyClustersManagerScheduler
from ._list_clusters_response_body import ListClustersResponseBodyClustersManager
from ._list_clusters_response_body import ListClustersResponseBodyClustersNodes
from ._list_clusters_response_body import ListClustersResponseBodyClustersUsers
from ._list_clusters_response_body import ListClustersResponseBodyClusters
from ._list_common_logs_response_body import ListCommonLogsResponseBodyLogs
from ._list_installed_softwares_response_body import ListInstalledSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfos
from ._list_installed_softwares_response_body import ListInstalledSoftwaresResponseBodyAdditionalPackages
from ._list_jobs_request import ListJobsRequestJobFilterDiagnosis
from ._list_jobs_request import ListJobsRequestJobFilterSortBy
from ._list_jobs_request import ListJobsRequestJobFilter
from ._list_jobs_response_body import ListJobsResponseBodyJobsJobSpecResources
from ._list_jobs_response_body import ListJobsResponseBodyJobsJobSpecResourcesActualOccupied
from ._list_jobs_response_body import ListJobsResponseBodyJobsJobSpec
from ._list_jobs_response_body import ListJobsResponseBodyJobs
from ._list_nodes_response_body import ListNodesResponseBodyNodesTotalResources
from ._list_nodes_response_body import ListNodesResponseBodyNodes
from ._list_queues_response_body import ListQueuesResponseBodyQueuesNodes
from ._list_queues_response_body import ListQueuesResponseBodyQueues
from ._list_regions_response_body import ListRegionsResponseBodyRegions
from ._list_shared_storages_response_body import ListSharedStoragesResponseBodySharedStoragesMountInfo
from ._list_shared_storages_response_body import ListSharedStoragesResponseBodySharedStorages
from ._list_softwares_request import ListSoftwaresRequestOsInfos
from ._list_softwares_response_body import ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfosVersionsVersionInfosSupportOsSupportOsInfos
from ._list_softwares_response_body import ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfosVersionsVersionInfosSupportOs
from ._list_softwares_response_body import ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfosVersionsVersionInfos
from ._list_softwares_response_body import ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfosVersions
from ._list_softwares_response_body import ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfos
from ._list_softwares_response_body import ListSoftwaresResponseBodyAdditionalPackages
from ._list_users_response_body import ListUsersResponseBodyUsersUserInfo
from ._list_users_response_body import ListUsersResponseBodyUsers
from ._uninstall_softwares_request import UninstallSoftwaresRequestAdditionalPackages
from ._update_cluster_request import UpdateClusterRequestClusterCustomConfiguration
from ._update_cluster_request import UpdateClusterRequestMonitorSpec
from ._update_cluster_request import UpdateClusterRequestSchedulerSpec
from ._update_nodes_request import UpdateNodesRequestInstances
from ._update_queue_request import UpdateQueueRequestQueue

__all__ = [
    AddonNodeTemplate,
    NodeTemplate,
    QueueTemplate,
    SharedStorageTemplate,
    AttachNodesRequest,
    AttachNodesShrinkRequest,
    AttachNodesResponseBody,
    AttachNodesResponse,
    AttachSharedStoragesRequest,
    AttachSharedStoragesShrinkRequest,
    AttachSharedStoragesResponseBody,
    AttachSharedStoragesResponse,
    CreateClusterRequest,
    CreateClusterShrinkRequest,
    CreateClusterResponseBody,
    CreateClusterResponse,
    CreateJobRequest,
    CreateJobShrinkRequest,
    CreateJobResponseBody,
    CreateJobResponse,
    CreateNodesRequest,
    CreateNodesShrinkRequest,
    CreateNodesResponseBody,
    CreateNodesResponse,
    CreateQueueRequest,
    CreateQueueShrinkRequest,
    CreateQueueResponseBody,
    CreateQueueResponse,
    CreateUsersRequest,
    CreateUsersShrinkRequest,
    CreateUsersResponseBody,
    CreateUsersResponse,
    DeleteClusterRequest,
    DeleteClusterResponseBody,
    DeleteClusterResponse,
    DeleteNodesRequest,
    DeleteNodesShrinkRequest,
    DeleteNodesResponseBody,
    DeleteNodesResponse,
    DeleteQueuesRequest,
    DeleteQueuesShrinkRequest,
    DeleteQueuesResponseBody,
    DeleteQueuesResponse,
    DeleteUsersRequest,
    DeleteUsersShrinkRequest,
    DeleteUsersResponseBody,
    DeleteUsersResponse,
    DescribeAddonTemplateRequest,
    DescribeAddonTemplateResponseBody,
    DescribeAddonTemplateResponse,
    DetachSharedStoragesRequest,
    DetachSharedStoragesShrinkRequest,
    DetachSharedStoragesResponseBody,
    DetachSharedStoragesResponse,
    GetAddonRequest,
    GetAddonResponseBody,
    GetAddonResponse,
    GetClusterRequest,
    GetClusterResponseBody,
    GetClusterResponse,
    GetCommonLogDetailRequest,
    GetCommonLogDetailResponseBody,
    GetCommonLogDetailResponse,
    GetJobRequest,
    GetJobResponseBody,
    GetJobResponse,
    GetJobLogRequest,
    GetJobLogResponseBody,
    GetJobLogResponse,
    GetQueueRequest,
    GetQueueResponseBody,
    GetQueueResponse,
    InstallAddonRequest,
    InstallAddonResponseBody,
    InstallAddonResponse,
    InstallSoftwaresRequest,
    InstallSoftwaresShrinkRequest,
    InstallSoftwaresResponseBody,
    InstallSoftwaresResponse,
    ListAddonTemplatesRequest,
    ListAddonTemplatesResponseBody,
    ListAddonTemplatesResponse,
    ListAddonsRequest,
    ListAddonsShrinkRequest,
    ListAddonsResponseBody,
    ListAddonsResponse,
    ListAvailableFileSystemsRequest,
    ListAvailableFileSystemsResponseBody,
    ListAvailableFileSystemsResponse,
    ListAvailableImagesRequest,
    ListAvailableImagesShrinkRequest,
    ListAvailableImagesResponseBody,
    ListAvailableImagesResponse,
    ListClustersRequest,
    ListClustersShrinkRequest,
    ListClustersResponseBody,
    ListClustersResponse,
    ListCommonLogsRequest,
    ListCommonLogsShrinkRequest,
    ListCommonLogsResponseBody,
    ListCommonLogsResponse,
    ListInstalledSoftwaresRequest,
    ListInstalledSoftwaresResponseBody,
    ListInstalledSoftwaresResponse,
    ListJobsRequest,
    ListJobsShrinkRequest,
    ListJobsResponseBody,
    ListJobsResponse,
    ListNodesRequest,
    ListNodesShrinkRequest,
    ListNodesResponseBody,
    ListNodesResponse,
    ListQueuesRequest,
    ListQueuesShrinkRequest,
    ListQueuesResponseBody,
    ListQueuesResponse,
    ListRegionsRequest,
    ListRegionsResponseBody,
    ListRegionsResponse,
    ListSharedStoragesRequest,
    ListSharedStoragesResponseBody,
    ListSharedStoragesResponse,
    ListSoftwaresRequest,
    ListSoftwaresResponseBody,
    ListSoftwaresResponse,
    ListUsersRequest,
    ListUsersResponseBody,
    ListUsersResponse,
    StopJobsRequest,
    StopJobsShrinkRequest,
    StopJobsResponseBody,
    StopJobsResponse,
    UnInstallAddonRequest,
    UnInstallAddonResponseBody,
    UnInstallAddonResponse,
    UninstallSoftwaresRequest,
    UninstallSoftwaresShrinkRequest,
    UninstallSoftwaresResponseBody,
    UninstallSoftwaresResponse,
    UpdateClusterRequest,
    UpdateClusterShrinkRequest,
    UpdateClusterResponseBody,
    UpdateClusterResponse,
    UpdateNodesRequest,
    UpdateNodesShrinkRequest,
    UpdateNodesResponseBody,
    UpdateNodesResponse,
    UpdateQueueRequest,
    UpdateQueueShrinkRequest,
    UpdateQueueResponseBody,
    UpdateQueueResponse,
    UpdateUserRequest,
    UpdateUserResponseBody,
    UpdateUserResponse,
    AddonNodeTemplateDataDisks,
    AddonNodeTemplateSystemDisk,
    NodeTemplateDataDisks,
    NodeTemplateSystemDisk,
    AttachNodesRequestComputeNode,
    AttachSharedStoragesRequestSharedStorages,
    CreateClusterRequestAdditionalPackages,
    CreateClusterRequestAddons,
    CreateClusterRequestClusterCredentials,
    CreateClusterRequestClusterCustomConfiguration,
    CreateClusterRequestManagerDNS,
    CreateClusterRequestManagerDirectoryService,
    CreateClusterRequestManagerScheduler,
    CreateClusterRequestManager,
    CreateClusterRequestTags,
    CreateJobRequestJobSpecResources,
    CreateJobRequestJobSpec,
    CreateUsersRequestUser,
    DeleteUsersRequestUser,
    DescribeAddonTemplateResponseBodyAddonResourcesSpecEipResource,
    DescribeAddonTemplateResponseBodyAddonResourcesSpec,
    DescribeAddonTemplateResponseBodyAddonServicesSpecInputParams,
    DescribeAddonTemplateResponseBodyAddonServicesSpecNetworkACL,
    DescribeAddonTemplateResponseBodyAddonServicesSpec,
    DescribeAddonTemplateResponseBodyAddon,
    DetachSharedStoragesRequestSharedStorages,
    GetAddonResponseBodyAddonResourcesSpecEipResource,
    GetAddonResponseBodyAddonResourcesSpec,
    GetAddonResponseBodyAddonServicesSpecInputParams,
    GetAddonResponseBodyAddonServicesSpecNetworkACL,
    GetAddonResponseBodyAddonServicesSpec,
    GetAddonResponseBodyAddon,
    GetClusterResponseBodyClusterCustomConfiguration,
    GetClusterResponseBodyManagerDNS,
    GetClusterResponseBodyManagerDirectoryService,
    GetClusterResponseBodyManagerManagerNodeSystemDisk,
    GetClusterResponseBodyManagerManagerNode,
    GetClusterResponseBodyManagerScheduler,
    GetClusterResponseBodyManager,
    GetClusterResponseBodyMonitorSpec,
    GetClusterResponseBodySchedulerSpec,
    GetCommonLogDetailResponseBodyLogDetailStages,
    GetCommonLogDetailResponseBodyLogDetail,
    GetJobResponseBodyJobInfoResources,
    GetJobResponseBodyJobInfoResourcesUsed,
    GetJobResponseBodyJobInfoVariables,
    GetJobResponseBodyJobInfo,
    GetQueueResponseBodyQueue,
    InstallSoftwaresRequestAdditionalPackages,
    ListAddonTemplatesResponseBodyAddons,
    ListAddonsResponseBodyAddons,
    ListAvailableFileSystemsResponseBodyFileSystemListMountTargetList,
    ListAvailableFileSystemsResponseBodyFileSystemList,
    ListAvailableImagesRequestDirectoryService,
    ListAvailableImagesRequestScheduler,
    ListAvailableImagesResponseBodyImages,
    ListClustersResponseBodyClustersAdditionalPackages,
    ListClustersResponseBodyClustersAddonsResourcesSpec,
    ListClustersResponseBodyClustersAddonsServicesSpec,
    ListClustersResponseBodyClustersAddons,
    ListClustersResponseBodyClustersClusterCustomConfiguration,
    ListClustersResponseBodyClustersManagerDNS,
    ListClustersResponseBodyClustersManagerDirectoryService,
    ListClustersResponseBodyClustersManagerScheduler,
    ListClustersResponseBodyClustersManager,
    ListClustersResponseBodyClustersNodes,
    ListClustersResponseBodyClustersUsers,
    ListClustersResponseBodyClusters,
    ListCommonLogsResponseBodyLogs,
    ListInstalledSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfos,
    ListInstalledSoftwaresResponseBodyAdditionalPackages,
    ListJobsRequestJobFilterDiagnosis,
    ListJobsRequestJobFilterSortBy,
    ListJobsRequestJobFilter,
    ListJobsResponseBodyJobsJobSpecResources,
    ListJobsResponseBodyJobsJobSpecResourcesActualOccupied,
    ListJobsResponseBodyJobsJobSpec,
    ListJobsResponseBodyJobs,
    ListNodesResponseBodyNodesTotalResources,
    ListNodesResponseBodyNodes,
    ListQueuesResponseBodyQueuesNodes,
    ListQueuesResponseBodyQueues,
    ListRegionsResponseBodyRegions,
    ListSharedStoragesResponseBodySharedStoragesMountInfo,
    ListSharedStoragesResponseBodySharedStorages,
    ListSoftwaresRequestOsInfos,
    ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfosVersionsVersionInfosSupportOsSupportOsInfos,
    ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfosVersionsVersionInfosSupportOs,
    ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfosVersionsVersionInfos,
    ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfosVersions,
    ListSoftwaresResponseBodyAdditionalPackagesAdditionalPackageInfos,
    ListSoftwaresResponseBodyAdditionalPackages,
    ListUsersResponseBodyUsersUserInfo,
    ListUsersResponseBodyUsers,
    UninstallSoftwaresRequestAdditionalPackages,
    UpdateClusterRequestClusterCustomConfiguration,
    UpdateClusterRequestMonitorSpec,
    UpdateClusterRequestSchedulerSpec,
    UpdateNodesRequestInstances,
    UpdateQueueRequestQueue
]
