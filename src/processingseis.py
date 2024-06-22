from obspy.signal.filter import bandpass

def preprocessar_dados(stream, freqmin, freqmax):
    """
    Aplica um filtro passa-banda aos dados sísmicos para remover ruídos.
    """
    traces = stream.traces
    for trace in traces:
        trace.data = bandpass(trace.data, freqmin, freqmax, df=trace.stats.sampling_rate)
    return stream
