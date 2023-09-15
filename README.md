## Pandas Database
### An extremely simple data storage system for python applications.

<b>to run in local mode (no dedicated server):</b><br>
git clone repo<br>
from pd-database import PandasDatabase<br>
pdb = PandasDatabase()<br>

<b>to run with a dedicated server:</b><br>
git clone repo<br>
docker run db-server<br>
import pdb-client<br>
pdb = PDClient()<br>