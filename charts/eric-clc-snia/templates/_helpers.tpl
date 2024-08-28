{{/* vim: set filetype=mustache: */}}

{{/*
Expand the name of the chart.
*/}}
{{- define "eric-clc-snia.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "eric-clc-snia.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Create chart version as used by the chart label.
*/}}
{{- define "eric-clc-snia.version" -}}
{{- printf "%s" .Chart.Version | replace "+" "_" | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Common annotations added to all resources
*/}}
{{- define "eric-clc-snia.common-annotations" }}
{{- template "eric-clc-snia.product-info" . }}
{{- if .Values.annotations }}
{{ toYaml .Values.annotations }}
{{- end }}
{{- end }}

{{/*
Create annotation for the product information (DR-D1121-064)
*/}}
{{- define "eric-clc-snia.product-info" -}}
ericsson.com/product-name: {{ (fromYaml (.Files.Get "eric-product-info.yaml")).productName | quote }}
ericsson.com/product-number: {{ (fromYaml (.Files.Get "eric-product-info.yaml")).productNumber | quote }}
ericsson.com/product-revision: {{ regexReplaceAll "(.*)[+|-].*" .Chart.Version "${1}" | quote }}
{{- end}}

{{/*
Define Labels
*/}}
{{- define "eric-clc-snia.labels" -}}
app.kubernetes.io/name: {{ template "eric-clc-snia.name" . }}
app.kubernetes.io/version: {{ template "eric-clc-snia.version" . }}
app.kubernetes.io/instance: {{ .Release.Name | quote }}
app: {{ template "eric-clc-snia.name" . }}
chart: {{ template "eric-clc-snia.chart" . }}
release: "{{ .Release.Name }}"
heritage: "{{ .Release.Service }}"
{{- if .Values.labels }}
{{ toYaml .Values.labels }}
{{- end }}
{{- end}}

{{/*
Define TLS, note: returns boolean as string
*/}}
{{- define "eric-clc-snia.tls" -}}
{{- $tlsEnabled := true -}}
{{- if .Values.global -}}
    {{- if .Values.global.security -}}
        {{- if .Values.global.security.tls -}}
            {{- if hasKey .Values.global.security.tls "enabled" -}}
                {{- $tlsEnabled = .Values.global.security.tls.enabled -}}
            {{- end -}}
        {{- end -}}
    {{- end -}}
{{- end -}}
{{- $tlsEnabled -}}
{{- end -}}