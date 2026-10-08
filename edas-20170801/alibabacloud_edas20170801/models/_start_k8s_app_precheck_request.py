# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartK8sAppPrecheckRequest(DaraModel):
    def __init__(
        self,
        annotations: str = None,
        app_id: str = None,
        app_name: str = None,
        cluster_id: str = None,
        component_ids: str = None,
        config_mount_descs: str = None,
        empty_dirs: str = None,
        env_froms: str = None,
        envs: str = None,
        image_url: str = None,
        java_start_up_config: str = None,
        labels: str = None,
        limit_ephemeral_storage: int = None,
        limit_mem: int = None,
        limitm_cpu: int = None,
        local_volume: str = None,
        namespace: str = None,
        package_url: str = None,
        pvc_mount_descs: str = None,
        region_id: str = None,
        replicas: int = None,
        requests_ephemeral_storage: int = None,
        requests_mem: int = None,
        requestsm_cpu: int = None,
    ):
        # The annotation of an application pod.
        self.annotations = annotations
        # The ID of the application.
        self.app_id = app_id
        # The name of the application. The name must start with a letter, and can contain digits, letters, and hyphens (-). It can be up to 36 characters in length.
        self.app_name = app_name
        # The ID of the cluster.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The ID of the application component. You can call the ListComponents operation to query application components. This parameter must be specified when the application runs in Apache Tomcat or in a standard Java application runtime environment. The Apache Tomcat application runtime environment is applicable to Dubbo applications that are deployed by using WAR packages. A standard Java application runtime environment is applicable to Spring Boot or Spring Cloud applications that are deployed by using JAR packages.
        # 
        # Valid values for regular application component IDs:
        # 
        # - 4: Apache Tomcat 7.0.91
        # 
        # - 5: OpenJDK 1.8.x
        # 
        # - 6: OpenJDK 1.7.x
        # 
        # - 7: Apache Tomcat 8.5.42
        # 
        # This parameter is available only for Java SDK 2.57.3 or later, or Python SDK 2.57.3 or later. Assume that you use an SDK that is not provided by Enterprise Distributed Application Service (EDAS), such as aliyun-python-sdk-core, aliyun-java-sdk-core, and Alibaba Cloud CLI. In this case, you can directly specify this parameter.
        self.component_ids = component_ids
        # The configuration for mounting a Kubernetes ConfigMap or Secret to a directory in an elastic container instance. The following parameters are included in the configuration:
        # 
        # - name: the name of the Kubernetes ConfigMap or Secret.
        # 
        # - type: the type of the API object that you want to mount. You can mount a Kubernetes ConfigMap or Secret.
        # 
        # - mountPath: the mount path. The mount path must be an absolute path that starts with a forward slash (/).
        self.config_mount_descs = config_mount_descs
        # The configuration for mounting a Kubernetes emptyDir volume to a directory in an elastic container instance. The following parameters are included in the configuration:
        # 
        # - mountPath: The mount path in the container. This parameter is required.
        # 
        # - readOnly: (Optional) The mount mode. The value true indicates the read-only mode. The value false indicates the read and write mode. Default value: false.
        # 
        # - subPathExpr: (Optional) The regular expression that is used to match the subdirectory.
        self.empty_dirs = empty_dirs
        # The Kubernetes environment variables that are configured in EnvFrom mode. A ConfigMap or Secret is mounted to a directory. Each key corresponds to a file in the directory, and the content of the file is the value of the key.
        # 
        # The following parameters are included in the configuration of the EnvFroms parameter:
        # 
        # - configMapRef: the ConfigMap that is referenced. The following parameter is included:
        # 
        #   name: the name of the ConfigMap.
        # 
        # - secretRef: the Secret that is referenced. The following parameter is included:
        # 
        #   name: the name of the Secret.
        self.env_froms = env_froms
        # The environment variables that are used to deploy the application. The value must be a JSON array. Valid values: regular environment variables, Kubernetes ConfigMap environment variables, and Kubernetes Secret environment variables. Specify regular environment variables in the following format:
        # 
        # `{"name":"x", "value": "y"}`
        # 
        # Specify Kubernetes ConfigMap environment variables in the following format to reference values from ConfigMaps:
        # 
        # `{ "name": "x2", "valueFrom": { "configMapKeyRef": { "name": "my-config", "key": "y2" } } }`
        # 
        # Specify Kubernetes Secret environment variables in the following format to reference values from Secrets:
        # 
        # `{ "name": "x3", "valueFrom": { "secretKeyRef": { "name": "my-secret", "key": "y3" } } }`
        # 
        # > If you want to cancel this configuration, set this parameter to an empty JSON array, which is in the format of "[]".
        self.envs = envs
        # The URL of the image.
        self.image_url = image_url
        # The configuration of Java startup parameters for a Java application. These startup parameters involve the memory, application, garbage collection (GC) policy, tools, service registration and discovery, and custom configurations. Proper parameter settings help reduce the GC overheads, shorten the server response time, and improve the throughput. Set this parameter to a JSON string. In the example, original indicates the configuration value, and startup indicates a startup parameter. The system automatically concatenates all startup values as the settings of Java startup parameters for the application. To delete this configuration, leave the parameter value empty by entering `""` or `"{}"`. The following parameters are included in the configuration:
        # 
        # - InitialHeapSize: the initial size of the heap memory.
        # 
        # - MaxHeapSize: the maximum size of the heap memory.
        # 
        # - CustomParams: the custom parameters, such as JVM -D parameters.
        # 
        # - Other parameters: You can view the JSON structure submitted by the frontend.
        self.java_start_up_config = java_start_up_config
        # The label of an application pod.
        self.labels = labels
        # The maximum size of space required by ephemeral storage. Unit: GB. The value 0 indicates that no limit is set on the ephemeral storage space.
        self.limit_ephemeral_storage = limit_ephemeral_storage
        # The maximum size of memory allowed for each application instance when the application is running. Unit: MB. The value of LimitMem must be greater than or equal to that of RequestsMem.
        self.limit_mem = limit_mem
        # The maximum number of CPU cores allowed for each application instance when the application is running. Unit: millicores. The value 0 indicates that no limit is set on CPU cores.
        self.limitm_cpu = limitm_cpu
        # The configurations that are used when the host files are mounted to the container on which the application is running. Example: `[{"type":"","nodePath":"/localfiles","mountPath":"/app/files"},{"type":"Directory","nodePath":"/mnt","mountPath":"/app/storage"}\\]`. Description:
        # 
        # - `nodePath`: the host path.
        # 
        # - `mountPath`: the path in the container.
        # 
        # - `type`: the mounting type.
        self.local_volume = local_volume
        # The namespace of the Kubernetes cluster. This parameter specifies the Kubernetes namespace in which your application is deployed. By default, the default namespace is used.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The URL of the deployment package.
        self.package_url = package_url
        # The configuration for mounting a Kubernetes PersistentVolumeClaim (PVC) to a directory in an elastic container instance. The following parameters are included in the configuration:
        # 
        # - pvcName: the name of the PVC. Make sure that the volume exists and is in the Bound state.
        # 
        # - mountPaths: the directory to which you want to mount the PVC. You can configure multiple directories. You can set the following two parameters for each mount directory:
        # 
        #   - mountPath: the mount path. The mount path must be an absolute path that starts with a forward slash (/).
        # 
        #   - readOnly: the mount mode. The value true indicates the read-only mode. The value false indicates the read and write mode. Default value: false.
        self.pvc_mount_descs = pvc_mount_descs
        # The ID of the region.
        self.region_id = region_id
        # The number of application instances.
        self.replicas = replicas
        # The minimum size of space required by ephemeral storage. Unit: GB. The value 0 indicates that no limit is set on the ephemeral storage space.
        self.requests_ephemeral_storage = requests_ephemeral_storage
        # The maximum size of memory allowed for each application instance when the application is created. Unit: MB. The value 0 indicates that no limit is set on the memory size. The value of RequestsMem cannot be greater than that of LimitMem.
        self.requests_mem = requests_mem
        # The maximum number of CPU cores allowed for each application instance when the application is created. Unit: millicores.
        self.requestsm_cpu = requestsm_cpu

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotations is not None:
            result['Annotations'] = self.annotations

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.component_ids is not None:
            result['ComponentIds'] = self.component_ids

        if self.config_mount_descs is not None:
            result['ConfigMountDescs'] = self.config_mount_descs

        if self.empty_dirs is not None:
            result['EmptyDirs'] = self.empty_dirs

        if self.env_froms is not None:
            result['EnvFroms'] = self.env_froms

        if self.envs is not None:
            result['Envs'] = self.envs

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.java_start_up_config is not None:
            result['JavaStartUpConfig'] = self.java_start_up_config

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.limit_ephemeral_storage is not None:
            result['LimitEphemeralStorage'] = self.limit_ephemeral_storage

        if self.limit_mem is not None:
            result['LimitMem'] = self.limit_mem

        if self.limitm_cpu is not None:
            result['LimitmCpu'] = self.limitm_cpu

        if self.local_volume is not None:
            result['LocalVolume'] = self.local_volume

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.package_url is not None:
            result['PackageUrl'] = self.package_url

        if self.pvc_mount_descs is not None:
            result['PvcMountDescs'] = self.pvc_mount_descs

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.replicas is not None:
            result['Replicas'] = self.replicas

        if self.requests_ephemeral_storage is not None:
            result['RequestsEphemeralStorage'] = self.requests_ephemeral_storage

        if self.requests_mem is not None:
            result['RequestsMem'] = self.requests_mem

        if self.requestsm_cpu is not None:
            result['RequestsmCpu'] = self.requestsm_cpu

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ComponentIds') is not None:
            self.component_ids = m.get('ComponentIds')

        if m.get('ConfigMountDescs') is not None:
            self.config_mount_descs = m.get('ConfigMountDescs')

        if m.get('EmptyDirs') is not None:
            self.empty_dirs = m.get('EmptyDirs')

        if m.get('EnvFroms') is not None:
            self.env_froms = m.get('EnvFroms')

        if m.get('Envs') is not None:
            self.envs = m.get('Envs')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('JavaStartUpConfig') is not None:
            self.java_start_up_config = m.get('JavaStartUpConfig')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('LimitEphemeralStorage') is not None:
            self.limit_ephemeral_storage = m.get('LimitEphemeralStorage')

        if m.get('LimitMem') is not None:
            self.limit_mem = m.get('LimitMem')

        if m.get('LimitmCpu') is not None:
            self.limitm_cpu = m.get('LimitmCpu')

        if m.get('LocalVolume') is not None:
            self.local_volume = m.get('LocalVolume')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('PackageUrl') is not None:
            self.package_url = m.get('PackageUrl')

        if m.get('PvcMountDescs') is not None:
            self.pvc_mount_descs = m.get('PvcMountDescs')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')

        if m.get('RequestsEphemeralStorage') is not None:
            self.requests_ephemeral_storage = m.get('RequestsEphemeralStorage')

        if m.get('RequestsMem') is not None:
            self.requests_mem = m.get('RequestsMem')

        if m.get('RequestsmCpu') is not None:
            self.requestsm_cpu = m.get('RequestsmCpu')

        return self

