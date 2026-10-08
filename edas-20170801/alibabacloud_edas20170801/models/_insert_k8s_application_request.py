# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InsertK8sApplicationRequest(DaraModel):
    def __init__(
        self,
        annotations: str = None,
        app_config: str = None,
        app_name: str = None,
        app_template_name: str = None,
        application_description: str = None,
        build_pack_id: str = None,
        cluster_id: str = None,
        command: str = None,
        command_args: str = None,
        config_mount_descs: str = None,
        container_registry_id: str = None,
        cs_cluster_id: str = None,
        custom_affinity: str = None,
        custom_agent_version: str = None,
        custom_tolerations: str = None,
        deploy_across_nodes: str = None,
        deploy_across_zones: str = None,
        edas_container_version: str = None,
        empty_dirs: str = None,
        enable_ahas: bool = None,
        enable_asm: bool = None,
        enable_empty_push_reject: bool = None,
        enable_lossless_rule: bool = None,
        env_froms: str = None,
        envs: str = None,
        feature_config: str = None,
        image_platforms: str = None,
        image_url: str = None,
        init_containers: str = None,
        internet_slb_id: str = None,
        internet_slb_port: int = None,
        internet_slb_protocol: str = None,
        internet_target_port: int = None,
        intranet_slb_id: str = None,
        intranet_slb_port: int = None,
        intranet_slb_protocol: str = None,
        intranet_target_port: int = None,
        is_multilingual_app: bool = None,
        jdk: str = None,
        java_start_up_config: str = None,
        labels: str = None,
        limit_cpu: int = None,
        limit_ephemeral_storage: int = None,
        limit_mem: int = None,
        limitm_cpu: int = None,
        liveness: str = None,
        local_volume: str = None,
        logical_region_id: str = None,
        lossless_rule_aligned: bool = None,
        lossless_rule_delay_time: int = None,
        lossless_rule_func_type: int = None,
        lossless_rule_related: bool = None,
        lossless_rule_warmup_time: int = None,
        mount_descs: str = None,
        namespace: str = None,
        nas_id: str = None,
        package_type: str = None,
        package_url: str = None,
        package_version: str = None,
        post_start: str = None,
        pre_stop: str = None,
        pvc_mount_descs: str = None,
        readiness: str = None,
        replicas: int = None,
        repo_id: str = None,
        requests_cpu: int = None,
        requests_ephemeral_storage: int = None,
        requests_mem: int = None,
        requestsm_cpu: int = None,
        resource_group_id: str = None,
        runtime_class_name: str = None,
        secret_name: str = None,
        security_context: str = None,
        service_configs: str = None,
        sidecars: str = None,
        sls_configs: str = None,
        startup: str = None,
        storage_type: str = None,
        terminate_grace_period: int = None,
        timeout: int = None,
        uri_encoding: str = None,
        use_body_encoding: bool = None,
        user_base_image_url: str = None,
        web_container: str = None,
        web_container_config: str = None,
        workload_type: str = None,
    ):
        # The annotations of the application pod.
        self.annotations = annotations
        # The application configuration when an application template is used. The value is a JSON string.
        self.app_config = app_config
        # The name of the application. The name must start with a letter and can contain digits, letters, and hyphens (-). The name can be up to 36 characters in length.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The name of the application template that is used to create the application. If you specify an application template when you create the application, the application template and the AppConfig parameter are preferentially used to determine the application configuration. Other configurations are ignored.
        self.app_template_name = app_template_name
        # The description of the application.
        self.application_description = application_description
        # The version of EDAS Container. This parameter conflicts with `EdasContainerVersion`. Use the `EdasContainerVersion` parameter instead.
        self.build_pack_id = build_pack_id
        # The ID of the cluster. You can call the ListCluster operation to query the cluster ID. For more information, see [ListCluster](https://help.aliyun.com/document_detail/154995.html).
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The startup command of the application. If you set this parameter, the original startup command of the image is overridden.
        self.command = command
        # The arguments for the startup command. The arguments are a JSON array of strings. Example: `[{"argument":"-c"},{"argument":"test"}]`. In this example, `-c` and `test` are two arguments.
        self.command_args = command_args
        # The configuration for mounting Kubernetes ConfigMaps and Secrets. You can mount ConfigMaps and Secrets to specified directories in a container. The following parameters are included in ConfigMountDescs:
        # 
        # - name: The name of the ConfigMap or Secret.
        # 
        # - type: The configuration type. Valid values: ConfigMap and Secret.
        # 
        # - mountPath: The mount path. The path must be an absolute path that starts with a forward slash (/).
        self.config_mount_descs = config_mount_descs
        # The ID of the repository that is used to build the image repository. If you leave this parameter empty, the default repository provided by EDAS is used. Currently, only the default repository provided by EDAS is supported.
        self.container_registry_id = container_registry_id
        # You must specify CsClusterId only when you create an application in a cluster that has never been imported.
        self.cs_cluster_id = cs_cluster_id
        # The custom affinity.
        self.custom_affinity = custom_affinity
        # The version of the agent.
        self.custom_agent_version = custom_agent_version
        # The custom tolerations.
        self.custom_tolerations = custom_tolerations
        # Specifies whether to distribute application instances to multiple nodes. A value of `true` means yes. Other values mean no.
        self.deploy_across_nodes = deploy_across_nodes
        # Specifies whether to distribute application instances to multiple zones. A value of `true` means yes. Other values mean no.
        self.deploy_across_zones = deploy_across_zones
        # The version of the `EDAS-Container` on which the deployment package depends.
        # 
        # > This parameter is not supported for image-based deployments.
        self.edas_container_version = edas_container_version
        # The configuration for mounting a Kubernetes emptyDir volume. You can mount an emptyDir volume to a specified directory in a container. The following parameters are included in EmptyDirs:
        # 
        # - mountPath: The mount path in the container. This parameter is required.
        # 
        # - readOnly: Specifies whether the volume is read-only. This parameter is optional. true specifies read-only. false specifies read and write. Default value: false.
        # 
        # - subPathExpr: The subdirectory expression. This parameter is optional.
        self.empty_dirs = empty_dirs
        # Specifies whether to enable Application High Availability Service (AHAS):
        # 
        # - true: Enable AHAS.
        # 
        # - false: Do not enable AHAS.
        self.enable_ahas = enable_ahas
        # You must set this parameter to true only when you create an application in a cluster that has never been imported and enable Service Mesh (ASM).
        self.enable_asm = enable_asm
        # Specifies whether to enable protection against empty pushes:
        # 
        # - true: Enable protection against empty pushes.
        # 
        # - false: Do not enable protection against empty pushes.
        self.enable_empty_push_reject = enable_empty_push_reject
        # Specifies whether to enable the graceful start rule:
        # 
        # - true: Enable the graceful start rule.
        # 
        # - false: Do not enable the graceful start rule.
        self.enable_lossless_rule = enable_lossless_rule
        # The configuration for environment variables of the Kubernetes EnvFrom type. You can mount a specified ConfigMap or Secret to a specified directory. Each key corresponds to a file in the directory. The content of the file is the value of the key.
        # 
        # The following parameters are included in EnvFroms:
        # 
        # - configMapRef: The reference to the ConfigMap. This field includes the following parameter:
        # 
        #   - name: The name of the ConfigMap.
        # 
        # - secretRef: The reference to the Secret. This field includes the following parameter:
        # 
        #   - name: The name of the Secret.
        self.env_froms = env_froms
        # The environment variables for the deployment. The value must be a JSON array of objects. Three types of environment variables are supported: regular environment variables, Kubernetes ConfigMap environment variables, and Kubernetes Secret environment variables. The format of a regular environment variable is as follows:
        # 
        # `{"name":"x", "value": "y"}`
        # 
        # You can use a ConfigMap to inject the value of a specific key into a container\\"s environment variable. The format is as follows:
        # 
        # `{ "name": "x2", "valueFrom": { "configMapKeyRef": { "name": "my-config", "key": "y2" } } }`
        # 
        # You can use a Secret to inject the value of a specific key into a container\\"s environment variable. The format is as follows:
        # 
        # `{ "name": "x3", "valueFrom": { "secretKeyRef": { "name": "my-secret", "key": "y3" } } }`
        # 
        # > To clear this configuration, set the value to an empty JSON array ([]).
        self.envs = envs
        # The configuration of the custom monitoring and administration solution.
        self.feature_config = feature_config
        # The architecture of the image platform. This parameter is valid when you use a WAR or JAR package for deployment. Examples:
        # 
        # - To specify the x86-64 architecture, enter linux/amd64.
        # 
        # - To specify the ARM64 architecture, enter linux/arm64.
        # 
        # - To build a dual-architecture image, enter linux/amd64,linux/arm64.
        # 
        # - If you do not enter a value, the default architecture is used.
        self.image_platforms = image_platforms
        # The address of the image. This parameter is required when you set `PackageType` to `Image`.
        self.image_url = image_url
        # The init containers for the application pod. You can set the container configuration in the YAML format. The value is the Base64-encoded YAML configuration of the init container.
        self.init_containers = init_containers
        # The ID of the internet-facing SLB instance. If you do not specify this parameter, EDAS automatically purchases a new SLB instance for you.
        self.internet_slb_id = internet_slb_id
        # The frontend port of the internet-facing SLB instance. The value must be in the range of 1 to 65535.
        self.internet_slb_port = internet_slb_port
        # The protocol used by the internet-facing SLB instance. Valid values: TCP, HTTP, and HTTPS.
        self.internet_slb_protocol = internet_slb_protocol
        # The backend port of the internal SLB instance, which also serves as the service port for the application. The port number must be an integer from 1 to 65535.
        self.internet_target_port = internet_target_port
        # The ID of the internal-facing SLB instance. If you do not specify this parameter, EDAS automatically purchases a new SLB instance for you.
        self.intranet_slb_id = intranet_slb_id
        # The frontend port of the internal-facing SLB instance. The value must be in the range of 1 to 65535.
        self.intranet_slb_port = intranet_slb_port
        # The protocol used by the internal-facing SLB instance. Valid values: TCP, HTTP, and HTTPS.
        self.intranet_slb_protocol = intranet_slb_protocol
        # The backend port of the internal-facing SLB instance. This is also the service port of the application. The value must be in the range of 1 to 65535.
        self.intranet_target_port = intranet_target_port
        # Specifies whether the application is a multilingual application.
        self.is_multilingual_app = is_multilingual_app
        # The version of the Java Development Kit (JDK) on which the deployment package depends. Valid values: Open JDK 7, Open JDK 8, and Custom OpenJDK. This parameter is not supported for image-based deployments. If you select Custom OpenJDK, you must also specify the UserBaseImageUrl parameter.
        self.jdk = jdk
        # The Java startup parameters. You can configure startup parameters for a Java application. You can configure memory, application, garbage collection (GC) policy, tools, service registration and discovery, and custom parameters. Proper parameter configuration helps reduce GC overhead, shorten server response time, and improve throughput. The value is a JSON string. original specifies the configuration value, and startup specifies the startup parameter. The system automatically concatenates all startup values as the Java startup parameters for the application. To clear the configuration, set the value to `""` or `"{}"`. The keys in the JSON string are described as follows:
        # 
        # - InitialHeapSize: the initial heap size.
        # 
        # - MaxHeapSize: the maximum heap size.
        # 
        # - CustomParams: custom content, such as JVM -D parameters.
        # 
        # - Other keys: You can view the JSON structure submitted by the frontend.
        self.java_start_up_config = java_start_up_config
        # The labels of the application pod.
        self.labels = labels
        # The maximum number of CPU cores that can be used by an application instance. If you specify LimitmCpu, this parameter is ignored.
        self.limit_cpu = limit_cpu
        # The maximum ephemeral storage. Unit: GB. A value of 0 means no limit.
        self.limit_ephemeral_storage = limit_ephemeral_storage
        # The maximum amount of memory that can be used by an application instance. Unit: MB. The value of LimitMem must be greater than or equal to the value of RequestsMem.
        self.limit_mem = limit_mem
        # The maximum number of CPU cores that can be used by an application instance. Unit: millicores. A value of 0 means no limit.
        self.limitm_cpu = limitm_cpu
        # The liveness probe of the container. Example: `{"failureThreshold": 3,"initialDelaySeconds": 5,"successThreshold": 1,"timeoutSeconds": 1,"tcpSocket":{"host":"", "port":8080}}`.
        # 
        # To clear this configuration, set the value to `""` or `{}`. If you do not set this parameter, it is ignored.
        self.liveness = liveness
        # The configuration for mounting a host file to a container. Example: `[{"type":"","nodePath":"/localfiles","mountPath":"/app/files"},{"type":"Directory","nodePath":"/mnt","mountPath":"/app/storage"}]`. The following parameters are included:
        # 
        # - `nodePath`: the path on the host.
        # 
        # - `mountPath`: the path in the container.
        # 
        # - `type`: the mount type.
        self.local_volume = local_volume
        # The ID of the EDAS namespace. This parameter is required if you want to use a non-default namespace.
        self.logical_region_id = logical_region_id
        # Specifies whether to enable the graceful rolling deployment mode in which service registration is complete before the readiness probe is passed:
        # 
        # - true: A health check URL is provided for the application on port 55199. The path is /health. The URL returns 200 after the service is registered. Otherwise, the URL returns 500.
        # 
        #   > If you also set `LosslessRuleRelated` to `true`, this URL is used to check whether the service warm-up is complete.
        # 
        # - false: A URL is not provided for the application to check whether the service is registered.
        self.lossless_rule_aligned = lossless_rule_aligned
        # The delay of service registration. Unit: seconds. The value must be in the range of 0 to 86400.
        self.lossless_rule_delay_time = lossless_rule_delay_time
        # The warm-up curve of the service. The value must be in the range of 0 to 20. Default value: 2. This value is suitable for normal warm-up scenarios and indicates that the traffic that the service provider receives follows a quadratic curve during the warm-up period.
        self.lossless_rule_func_type = lossless_rule_func_type
        # Specifies whether to enable the graceful rolling deployment mode in which service warm-up is complete before the readiness probe is passed:
        # 
        # - true: A health check URL is provided for the application on port 55199. The path is /health. The URL returns 200 after the service warm-up is complete. Otherwise, the URL returns 500.
        # 
        # - false: A URL is not provided for the application to check whether the service warm-up is complete.
        self.lossless_rule_related = lossless_rule_related
        # The warm-up duration of the service. Unit: seconds. The value must be in the range of 0 to 86400.
        self.lossless_rule_warmup_time = lossless_rule_warmup_time
        # The description of the mount configuration. The value is a serialized JSON string. Example: `[{"nasPath": "/k8s","mountPath": "/mnt"},{"nasPath": "/files","mountPath": "/app/files"}]`. `nasPath` specifies the file storage path. `mountPath` specifies the path to which the file system is mounted in the container.
        self.mount_descs = mount_descs
        # The namespace of the Kubernetes cluster. This parameter determines the Kubernetes namespace in which your application is deployed. The default value is default.
        self.namespace = namespace
        # The ID of the NAS file system that you want to mount. If you do not specify this parameter but mountDescs is specified, a new NAS file system is automatically purchased and mounted to a vSwitch in the VPC.
        self.nas_id = nas_id
        # The type of the application package. Valid values: FatJar, WAR, and Image.
        self.package_type = package_type
        # The URL of the deployment package. This parameter is required for applications that are deployed using a FatJar or WAR package.
        # 
        # > The version of the EDAS POP API SDK for Java or Python must be 2.44.0 or later.
        self.package_url = package_url
        # The version number of the deployment package. This parameter is required for WAR and FatJar packages. You can define the meaning of the version number.
        # 
        # > The version of the EDAS POP API SDK for Java or Python must be 2.44.0 or later.
        self.package_version = package_version
        # The script that is run after the container is started. Example: `{"exec":{"command":["cat","/etc/group"]}}`.
        # 
        # To clear this configuration, set the value to `""` or `{}`. If you do not set this parameter, it is ignored.
        self.post_start = post_start
        # The script that is run before the container is stopped. Example: `{"tcpSocket":{"host":"", "port":8080}}`.
        # 
        # To clear this configuration, set the value to `""` or `{}`. If you do not set this parameter, it is ignored.
        self.pre_stop = pre_stop
        # The configuration for mounting a Kubernetes PersistentVolumeClaim (PVC). You can mount a Kubernetes PVC volume to a specified directory in a container. The following parameters are included in PvcMountDescs:
        # 
        # - pvcName: The name of the PVC volume. The PVC volume must exist and be in the Bound state.
        # 
        # - mountPaths: The list of mount directories. You can configure multiple mount directories. Each mount directory supports two parameters.
        # 
        #   - mountPath: The mount path. The path must be an absolute path that starts with a forward slash (/).
        # 
        #   - readOnly: The mount mode. true specifies the read-only mode. false specifies the read and write mode. Default value: false.
        self.pvc_mount_descs = pvc_mount_descs
        # The readiness probe of the container. If the check fails, traffic is not routed to the container through the Kubernetes Service. Example: `{"failureThreshold": 3,"initialDelaySeconds": 5,"successThreshold": 1,"timeoutSeconds": 1,"httpGet": {"path": "/consumer","port": 8080,"scheme": "HTTP","httpHeaders": [{"name": "test","value": "testvalue"}]}}`.
        # 
        # To clear this configuration, set the value to `""` or `{}`. If you do not set this parameter, it is ignored.
        self.readiness = readiness
        # The number of application instances.
        self.replicas = replicas
        # The ID of the image repository.
        self.repo_id = repo_id
        # The number of CPU cores requested for an application instance upon creation. Unit: cores. A value of 0 means no limit. If you specify RequestsmCpu, this parameter is ignored.
        self.requests_cpu = requests_cpu
        # The minimum ephemeral storage. Unit: GB. A value of 0 means no limit.
        self.requests_ephemeral_storage = requests_ephemeral_storage
        # The amount of memory requested for an application instance upon creation. Unit: MB. A value of 0 means no limit. The value of RequestsMem cannot be greater than the value of LimitMem.
        self.requests_mem = requests_mem
        # The number of CPU cores requested for an application instance upon creation. Unit: millicores.
        self.requestsm_cpu = requestsm_cpu
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The type of the container runtime. This parameter is applicable only to clusters that use sandboxed containers.
        self.runtime_class_name = runtime_class_name
        # The name of the image pull secret. You must create the secret.
        self.secret_name = secret_name
        # The SecurityContext attribute for the application pod container. The value is the Base64-encoded YAML configuration of the SecurityContext.
        self.security_context = security_context
        # The configuration of the Kubernetes Service.
        self.service_configs = service_configs
        # The sidecar containers for the application pod. You can set the container configuration in the YAML format. The value is the Base64-encoded YAML configuration of the sidecar container.
        self.sidecars = sidecars
        # The Logstore configuration. To clear the configuration, set the value to `""` or `"{}"`:
        # 
        # - Configs:
        # 
        #   - type: The collection type. file indicates the file type. stdout indicates the standard output type.
        # 
        #   - Logstore: The name of the Logstore. Make sure that the Logstore name is unique in the same cluster and meets the following naming conventions:
        # 
        #     - The name can contain only lowercase letters, digits, hyphens (-), and underscores (_).
        # 
        #     - The name must start and end with a lowercase letter or a digit.
        # 
        #     - The name must be 3 to 63 characters in length. If you leave this parameter empty, the system automatically generates a name.
        # 
        #   - LogDir: If the collection type is standard output, the collection path is stdout.log. If the collection type is file, the collection path is the path of the file to be collected. Wildcards are supported. The collection path must match the following regular expression: `^/(.+)/(.*)^/$`.
        self.sls_configs = sls_configs
        # The startup probe. You can use a startup probe to check the liveness of a slow-start container and prevent the container from being killed before it is started. Example: {"failureThreshold": 3,"initialDelaySeconds": 5,"successThreshold": 1,"timeoutSeconds": 1,"httpGet": {"path": "/consumer","port": 8080,"scheme": "HTTP","httpHeaders": [{"name": "test","value": "testvalue"}]}}.
        # 
        # To clear this configuration, set the value to "" or {}. If you do not set this parameter, it is ignored.
        self.startup = startup
        # The storage type of the NAS file system. Valid values:
        # 
        # - General-purpose NAS file systems: Capacity and Performance
        # 
        # - Extreme NAS file systems: Standard and Advance
        # 
        # Currently, only the Performance type is supported.
        self.storage_type = storage_type
        # The timeout period for a graceful stop. Unit: seconds.
        self.terminate_grace_period = terminate_grace_period
        # The timeout period for the change process. Unit: seconds. The value must be in the range of 1 to 1800. If you do not specify this parameter, the default value 1800 is used.
        self.timeout = timeout
        # The URI encoding scheme. Valid values: ISO-8859-1, GBK, GB2312, and UTF-8.
        # 
        # > If you do not set this parameter for the application, the default value of Tomcat is used.
        self.uri_encoding = uri_encoding
        # Specifies whether to enable useBodyEncodingForURI.
        # 
        # > If you do not set this parameter for the application, the default value false is used.
        self.use_body_encoding = use_body_encoding
        # If you use a custom JDK runtime, you must configure the address of the base image. The address must be accessible over the Internet. The EDAS server pulls the image to build an application image.
        self.user_base_image_url = user_base_image_url
        # The version of the Tomcat container on which the deployment package depends. This parameter is applicable to Spring Cloud and Dubbo applications that are deployed using a WAR package. This parameter is not supported for image-based deployments.
        self.web_container = web_container
        # The configuration of the Tomcat container. To clear the configuration, set the value to "" or "{}":
        # 
        # - useDefaultConfig: Specifies whether to use the default configuration. If you set this parameter to true, the custom configuration is not used. If you set this parameter to false, the custom configuration is used. If you do not use the custom configuration, the following parameter settings do not take effect.
        # 
        # - contextInputType: The access path of the application.
        # 
        #   - war: You do not need to specify a custom path. The access path is the name of the WAR package.
        # 
        #   - root: You do not need to specify a custom path. The access path is `/`.
        # 
        #   - custom: You must specify a custom path in the contextPath parameter.
        # 
        # - contextPath: The custom path. This parameter is required only when you set contextInputType to custom.
        # 
        # - httpPort: The port number. The value must be in the range of 1024 to 65535. Ports smaller than 1024 require root permissions. Because the container is configured with administrator permissions, specify a port number greater than 1024. If you do not specify this parameter, the default port 8080 is used.
        # 
        # - maxThreads: The maximum number of connections in the connection pool. Default value: 400.
        # 
        #   > This parameter greatly affects application performance. Configure this parameter with the help of a professional.
        # 
        # - uriEncoding: The encoding format for Tomcat. Valid values: UTF-8, ISO-8859-1, GBK, and GB2312. If you do not specify this parameter, the default value ISO-8859-1 is used.
        # 
        # - useBodyEncoding: Specifies whether to use BodyEncoding for URLs.
        # 
        # - useAdvancedServerXml: Specifies whether to use advanced settings to customize the server.xml file. If the preceding parameter types and specific parameters cannot meet your requirements, you can use advanced settings to directly edit the server.xml file of Tomcat.
        # 
        # - serverXml: The content of the server.xml file that is customized in the advanced settings. This parameter takes effect only when useAdvancedServerXml is set to true.
        self.web_container_config = web_container_config
        # The type of the workload. Currently, only deployments are supported.
        self.workload_type = workload_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotations is not None:
            result['Annotations'] = self.annotations

        if self.app_config is not None:
            result['AppConfig'] = self.app_config

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_template_name is not None:
            result['AppTemplateName'] = self.app_template_name

        if self.application_description is not None:
            result['ApplicationDescription'] = self.application_description

        if self.build_pack_id is not None:
            result['BuildPackId'] = self.build_pack_id

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.command is not None:
            result['Command'] = self.command

        if self.command_args is not None:
            result['CommandArgs'] = self.command_args

        if self.config_mount_descs is not None:
            result['ConfigMountDescs'] = self.config_mount_descs

        if self.container_registry_id is not None:
            result['ContainerRegistryId'] = self.container_registry_id

        if self.cs_cluster_id is not None:
            result['CsClusterId'] = self.cs_cluster_id

        if self.custom_affinity is not None:
            result['CustomAffinity'] = self.custom_affinity

        if self.custom_agent_version is not None:
            result['CustomAgentVersion'] = self.custom_agent_version

        if self.custom_tolerations is not None:
            result['CustomTolerations'] = self.custom_tolerations

        if self.deploy_across_nodes is not None:
            result['DeployAcrossNodes'] = self.deploy_across_nodes

        if self.deploy_across_zones is not None:
            result['DeployAcrossZones'] = self.deploy_across_zones

        if self.edas_container_version is not None:
            result['EdasContainerVersion'] = self.edas_container_version

        if self.empty_dirs is not None:
            result['EmptyDirs'] = self.empty_dirs

        if self.enable_ahas is not None:
            result['EnableAhas'] = self.enable_ahas

        if self.enable_asm is not None:
            result['EnableAsm'] = self.enable_asm

        if self.enable_empty_push_reject is not None:
            result['EnableEmptyPushReject'] = self.enable_empty_push_reject

        if self.enable_lossless_rule is not None:
            result['EnableLosslessRule'] = self.enable_lossless_rule

        if self.env_froms is not None:
            result['EnvFroms'] = self.env_froms

        if self.envs is not None:
            result['Envs'] = self.envs

        if self.feature_config is not None:
            result['FeatureConfig'] = self.feature_config

        if self.image_platforms is not None:
            result['ImagePlatforms'] = self.image_platforms

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.init_containers is not None:
            result['InitContainers'] = self.init_containers

        if self.internet_slb_id is not None:
            result['InternetSlbId'] = self.internet_slb_id

        if self.internet_slb_port is not None:
            result['InternetSlbPort'] = self.internet_slb_port

        if self.internet_slb_protocol is not None:
            result['InternetSlbProtocol'] = self.internet_slb_protocol

        if self.internet_target_port is not None:
            result['InternetTargetPort'] = self.internet_target_port

        if self.intranet_slb_id is not None:
            result['IntranetSlbId'] = self.intranet_slb_id

        if self.intranet_slb_port is not None:
            result['IntranetSlbPort'] = self.intranet_slb_port

        if self.intranet_slb_protocol is not None:
            result['IntranetSlbProtocol'] = self.intranet_slb_protocol

        if self.intranet_target_port is not None:
            result['IntranetTargetPort'] = self.intranet_target_port

        if self.is_multilingual_app is not None:
            result['IsMultilingualApp'] = self.is_multilingual_app

        if self.jdk is not None:
            result['JDK'] = self.jdk

        if self.java_start_up_config is not None:
            result['JavaStartUpConfig'] = self.java_start_up_config

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.limit_cpu is not None:
            result['LimitCpu'] = self.limit_cpu

        if self.limit_ephemeral_storage is not None:
            result['LimitEphemeralStorage'] = self.limit_ephemeral_storage

        if self.limit_mem is not None:
            result['LimitMem'] = self.limit_mem

        if self.limitm_cpu is not None:
            result['LimitmCpu'] = self.limitm_cpu

        if self.liveness is not None:
            result['Liveness'] = self.liveness

        if self.local_volume is not None:
            result['LocalVolume'] = self.local_volume

        if self.logical_region_id is not None:
            result['LogicalRegionId'] = self.logical_region_id

        if self.lossless_rule_aligned is not None:
            result['LosslessRuleAligned'] = self.lossless_rule_aligned

        if self.lossless_rule_delay_time is not None:
            result['LosslessRuleDelayTime'] = self.lossless_rule_delay_time

        if self.lossless_rule_func_type is not None:
            result['LosslessRuleFuncType'] = self.lossless_rule_func_type

        if self.lossless_rule_related is not None:
            result['LosslessRuleRelated'] = self.lossless_rule_related

        if self.lossless_rule_warmup_time is not None:
            result['LosslessRuleWarmupTime'] = self.lossless_rule_warmup_time

        if self.mount_descs is not None:
            result['MountDescs'] = self.mount_descs

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.nas_id is not None:
            result['NasId'] = self.nas_id

        if self.package_type is not None:
            result['PackageType'] = self.package_type

        if self.package_url is not None:
            result['PackageUrl'] = self.package_url

        if self.package_version is not None:
            result['PackageVersion'] = self.package_version

        if self.post_start is not None:
            result['PostStart'] = self.post_start

        if self.pre_stop is not None:
            result['PreStop'] = self.pre_stop

        if self.pvc_mount_descs is not None:
            result['PvcMountDescs'] = self.pvc_mount_descs

        if self.readiness is not None:
            result['Readiness'] = self.readiness

        if self.replicas is not None:
            result['Replicas'] = self.replicas

        if self.repo_id is not None:
            result['RepoId'] = self.repo_id

        if self.requests_cpu is not None:
            result['RequestsCpu'] = self.requests_cpu

        if self.requests_ephemeral_storage is not None:
            result['RequestsEphemeralStorage'] = self.requests_ephemeral_storage

        if self.requests_mem is not None:
            result['RequestsMem'] = self.requests_mem

        if self.requestsm_cpu is not None:
            result['RequestsmCpu'] = self.requestsm_cpu

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.runtime_class_name is not None:
            result['RuntimeClassName'] = self.runtime_class_name

        if self.secret_name is not None:
            result['SecretName'] = self.secret_name

        if self.security_context is not None:
            result['SecurityContext'] = self.security_context

        if self.service_configs is not None:
            result['ServiceConfigs'] = self.service_configs

        if self.sidecars is not None:
            result['Sidecars'] = self.sidecars

        if self.sls_configs is not None:
            result['SlsConfigs'] = self.sls_configs

        if self.startup is not None:
            result['Startup'] = self.startup

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.terminate_grace_period is not None:
            result['TerminateGracePeriod'] = self.terminate_grace_period

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.uri_encoding is not None:
            result['UriEncoding'] = self.uri_encoding

        if self.use_body_encoding is not None:
            result['UseBodyEncoding'] = self.use_body_encoding

        if self.user_base_image_url is not None:
            result['UserBaseImageUrl'] = self.user_base_image_url

        if self.web_container is not None:
            result['WebContainer'] = self.web_container

        if self.web_container_config is not None:
            result['WebContainerConfig'] = self.web_container_config

        if self.workload_type is not None:
            result['WorkloadType'] = self.workload_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')

        if m.get('AppConfig') is not None:
            self.app_config = m.get('AppConfig')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppTemplateName') is not None:
            self.app_template_name = m.get('AppTemplateName')

        if m.get('ApplicationDescription') is not None:
            self.application_description = m.get('ApplicationDescription')

        if m.get('BuildPackId') is not None:
            self.build_pack_id = m.get('BuildPackId')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Command') is not None:
            self.command = m.get('Command')

        if m.get('CommandArgs') is not None:
            self.command_args = m.get('CommandArgs')

        if m.get('ConfigMountDescs') is not None:
            self.config_mount_descs = m.get('ConfigMountDescs')

        if m.get('ContainerRegistryId') is not None:
            self.container_registry_id = m.get('ContainerRegistryId')

        if m.get('CsClusterId') is not None:
            self.cs_cluster_id = m.get('CsClusterId')

        if m.get('CustomAffinity') is not None:
            self.custom_affinity = m.get('CustomAffinity')

        if m.get('CustomAgentVersion') is not None:
            self.custom_agent_version = m.get('CustomAgentVersion')

        if m.get('CustomTolerations') is not None:
            self.custom_tolerations = m.get('CustomTolerations')

        if m.get('DeployAcrossNodes') is not None:
            self.deploy_across_nodes = m.get('DeployAcrossNodes')

        if m.get('DeployAcrossZones') is not None:
            self.deploy_across_zones = m.get('DeployAcrossZones')

        if m.get('EdasContainerVersion') is not None:
            self.edas_container_version = m.get('EdasContainerVersion')

        if m.get('EmptyDirs') is not None:
            self.empty_dirs = m.get('EmptyDirs')

        if m.get('EnableAhas') is not None:
            self.enable_ahas = m.get('EnableAhas')

        if m.get('EnableAsm') is not None:
            self.enable_asm = m.get('EnableAsm')

        if m.get('EnableEmptyPushReject') is not None:
            self.enable_empty_push_reject = m.get('EnableEmptyPushReject')

        if m.get('EnableLosslessRule') is not None:
            self.enable_lossless_rule = m.get('EnableLosslessRule')

        if m.get('EnvFroms') is not None:
            self.env_froms = m.get('EnvFroms')

        if m.get('Envs') is not None:
            self.envs = m.get('Envs')

        if m.get('FeatureConfig') is not None:
            self.feature_config = m.get('FeatureConfig')

        if m.get('ImagePlatforms') is not None:
            self.image_platforms = m.get('ImagePlatforms')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('InitContainers') is not None:
            self.init_containers = m.get('InitContainers')

        if m.get('InternetSlbId') is not None:
            self.internet_slb_id = m.get('InternetSlbId')

        if m.get('InternetSlbPort') is not None:
            self.internet_slb_port = m.get('InternetSlbPort')

        if m.get('InternetSlbProtocol') is not None:
            self.internet_slb_protocol = m.get('InternetSlbProtocol')

        if m.get('InternetTargetPort') is not None:
            self.internet_target_port = m.get('InternetTargetPort')

        if m.get('IntranetSlbId') is not None:
            self.intranet_slb_id = m.get('IntranetSlbId')

        if m.get('IntranetSlbPort') is not None:
            self.intranet_slb_port = m.get('IntranetSlbPort')

        if m.get('IntranetSlbProtocol') is not None:
            self.intranet_slb_protocol = m.get('IntranetSlbProtocol')

        if m.get('IntranetTargetPort') is not None:
            self.intranet_target_port = m.get('IntranetTargetPort')

        if m.get('IsMultilingualApp') is not None:
            self.is_multilingual_app = m.get('IsMultilingualApp')

        if m.get('JDK') is not None:
            self.jdk = m.get('JDK')

        if m.get('JavaStartUpConfig') is not None:
            self.java_start_up_config = m.get('JavaStartUpConfig')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('LimitCpu') is not None:
            self.limit_cpu = m.get('LimitCpu')

        if m.get('LimitEphemeralStorage') is not None:
            self.limit_ephemeral_storage = m.get('LimitEphemeralStorage')

        if m.get('LimitMem') is not None:
            self.limit_mem = m.get('LimitMem')

        if m.get('LimitmCpu') is not None:
            self.limitm_cpu = m.get('LimitmCpu')

        if m.get('Liveness') is not None:
            self.liveness = m.get('Liveness')

        if m.get('LocalVolume') is not None:
            self.local_volume = m.get('LocalVolume')

        if m.get('LogicalRegionId') is not None:
            self.logical_region_id = m.get('LogicalRegionId')

        if m.get('LosslessRuleAligned') is not None:
            self.lossless_rule_aligned = m.get('LosslessRuleAligned')

        if m.get('LosslessRuleDelayTime') is not None:
            self.lossless_rule_delay_time = m.get('LosslessRuleDelayTime')

        if m.get('LosslessRuleFuncType') is not None:
            self.lossless_rule_func_type = m.get('LosslessRuleFuncType')

        if m.get('LosslessRuleRelated') is not None:
            self.lossless_rule_related = m.get('LosslessRuleRelated')

        if m.get('LosslessRuleWarmupTime') is not None:
            self.lossless_rule_warmup_time = m.get('LosslessRuleWarmupTime')

        if m.get('MountDescs') is not None:
            self.mount_descs = m.get('MountDescs')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NasId') is not None:
            self.nas_id = m.get('NasId')

        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')

        if m.get('PackageUrl') is not None:
            self.package_url = m.get('PackageUrl')

        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')

        if m.get('PostStart') is not None:
            self.post_start = m.get('PostStart')

        if m.get('PreStop') is not None:
            self.pre_stop = m.get('PreStop')

        if m.get('PvcMountDescs') is not None:
            self.pvc_mount_descs = m.get('PvcMountDescs')

        if m.get('Readiness') is not None:
            self.readiness = m.get('Readiness')

        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        if m.get('RequestsCpu') is not None:
            self.requests_cpu = m.get('RequestsCpu')

        if m.get('RequestsEphemeralStorage') is not None:
            self.requests_ephemeral_storage = m.get('RequestsEphemeralStorage')

        if m.get('RequestsMem') is not None:
            self.requests_mem = m.get('RequestsMem')

        if m.get('RequestsmCpu') is not None:
            self.requestsm_cpu = m.get('RequestsmCpu')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RuntimeClassName') is not None:
            self.runtime_class_name = m.get('RuntimeClassName')

        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')

        if m.get('SecurityContext') is not None:
            self.security_context = m.get('SecurityContext')

        if m.get('ServiceConfigs') is not None:
            self.service_configs = m.get('ServiceConfigs')

        if m.get('Sidecars') is not None:
            self.sidecars = m.get('Sidecars')

        if m.get('SlsConfigs') is not None:
            self.sls_configs = m.get('SlsConfigs')

        if m.get('Startup') is not None:
            self.startup = m.get('Startup')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('TerminateGracePeriod') is not None:
            self.terminate_grace_period = m.get('TerminateGracePeriod')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('UriEncoding') is not None:
            self.uri_encoding = m.get('UriEncoding')

        if m.get('UseBodyEncoding') is not None:
            self.use_body_encoding = m.get('UseBodyEncoding')

        if m.get('UserBaseImageUrl') is not None:
            self.user_base_image_url = m.get('UserBaseImageUrl')

        if m.get('WebContainer') is not None:
            self.web_container = m.get('WebContainer')

        if m.get('WebContainerConfig') is not None:
            self.web_container_config = m.get('WebContainerConfig')

        if m.get('WorkloadType') is not None:
            self.workload_type = m.get('WorkloadType')

        return self

